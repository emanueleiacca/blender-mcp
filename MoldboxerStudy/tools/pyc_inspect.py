"""
pyc_inspect.py — extract a readable "shape" view from a .pyc compiled with
Python 3.11. Uses only the stdlib (marshal + dis), so no third-party install.

For each .pyc it produces a markdown-like text dump with:
  - module-level docstring
  - imports (recovered from bytecode IMPORT_NAME / IMPORT_FROM ops)
  - constants/string pool
  - class definitions + method names + signatures + docstrings
  - top-level function definitions + signatures + docstrings
  - a disassembly per function (compact)

Run with the SAME Python version that produced the .pyc (3.11), otherwise
marshal.loads may refuse the bytecode.

Usage:
  python pyc_inspect.py <input.pyc> [output.txt]
  python pyc_inspect.py --tree <folder>            # walk all .pyc in folder
"""

from __future__ import annotations

import dis
import marshal
import os
import struct
import sys
import textwrap
import types
from pathlib import Path


PYC_HEADER_LEN_311 = 16  # magic(4) + flags(4) + mtime/hash(4) + size(4)


def load_code(pyc_path: Path) -> types.CodeType:
    raw = pyc_path.read_bytes()
    magic = struct.unpack("<I", raw[:4])[0]
    if magic != 0xA70D0D0A:
        print(f"WARN: {pyc_path.name} magic={hex(magic)} (expected 0xa70d0d0a for Py3.11)", file=sys.stderr)
    return marshal.loads(raw[PYC_HEADER_LEN_311:])


def iter_codes(code: types.CodeType):
    yield code
    for const in code.co_consts:
        if isinstance(const, types.CodeType):
            yield from iter_codes(const)


def format_signature(code: types.CodeType) -> str:
    argcount = code.co_argcount
    posonly = code.co_posonlyargcount
    kwonly = code.co_kwonlyargcount
    varnames = list(code.co_varnames)
    args = varnames[:argcount]
    kwonlies = varnames[argcount:argcount + kwonly]
    parts = list(args)
    if posonly:
        parts.insert(posonly, "/")
    if code.co_flags & 0x04:  # *args
        parts.append(f"*{varnames[argcount + kwonly]}")
    elif kwonlies:
        parts.append("*")
    parts.extend(kwonlies)
    if code.co_flags & 0x08:  # **kwargs
        rest_idx = argcount + kwonly + (1 if code.co_flags & 0x04 else 0)
        parts.append(f"**{varnames[rest_idx]}")
    return f"({', '.join(parts)})"


def first_docstring(code: types.CodeType) -> str | None:
    if not code.co_consts:
        return None
    first = code.co_consts[0]
    if isinstance(first, str) and first.strip():
        return first
    return None


def recover_imports(code: types.CodeType) -> list[str]:
    out: list[str] = []
    instructions = list(dis.get_instructions(code))
    i = 0
    while i < len(instructions):
        ins = instructions[i]
        if ins.opname == "IMPORT_NAME":
            mod = ins.argval
            # look ahead for IMPORT_FROM ops attached to this import
            froms = []
            j = i + 1
            while j < len(instructions) and instructions[j].opname in {"IMPORT_FROM", "STORE_NAME", "STORE_FAST", "STORE_GLOBAL", "POP_TOP"}:
                if instructions[j].opname == "IMPORT_FROM":
                    froms.append(instructions[j].argval)
                j += 1
            if froms:
                out.append(f"from {mod} import {', '.join(froms)}")
            else:
                out.append(f"import {mod}")
        i += 1
    # also scan nested codes (e.g. functions doing late imports)
    return out


def collect_classes_and_funcs(code: types.CodeType):
    """Walk the code object, returning (top_level_funcs, classes).

    classes is a list of dicts: {name, bases, methods: [(name, sig, doc)], doc}
    top_level_funcs is a list of (name, sig, doc).
    """
    classes = []
    top_funcs = []

    consts = list(code.co_consts)
    # In Python 3.11, class body code objects have co_name == class name.
    # Top-level functions appear as code objects in co_consts with co_name == func name.

    instructions = list(dis.get_instructions(code))

    # Map MAKE_FUNCTION -> the function code by looking at preceding LOAD_CONST<code>.
    # MAKE_CLASS uses LOAD_BUILD_CLASS / call pattern.

    # Pass 1: find class definitions via LOAD_BUILD_CLASS pattern.
    for i, ins in enumerate(instructions):
        if ins.opname == "LOAD_BUILD_CLASS":
            # Walk forward; the next LOAD_CONST holding a code object whose co_name
            # is a class body is the class.
            for j in range(i + 1, min(i + 8, len(instructions))):
                arg = instructions[j].argval
                if isinstance(arg, types.CodeType) and arg.co_name != "<lambda>":
                    body_code = arg
                    cls_name = body_code.co_name
                    # bases come from later instructions until CALL — argval names follow LOAD_NAME/LOAD_GLOBAL
                    bases = []
                    for k in range(j + 1, min(j + 12, len(instructions))):
                        bins = instructions[k]
                        if bins.opname in {"LOAD_NAME", "LOAD_GLOBAL"} and isinstance(bins.argval, str):
                            bases.append(bins.argval)
                        if bins.opname in {"CALL", "PRECALL"}:
                            break
                    methods = []
                    for m_const in body_code.co_consts:
                        if isinstance(m_const, types.CodeType) and m_const.co_name not in {"<lambda>", "<dictcomp>", "<listcomp>", "<setcomp>", "<genexpr>"}:
                            methods.append((
                                m_const.co_name,
                                format_signature(m_const),
                                first_docstring(m_const),
                            ))
                    classes.append({
                        "name": cls_name,
                        "bases": bases,
                        "doc": first_docstring(body_code),
                        "methods": methods,
                    })
                    break

    # Pass 2: top-level functions = code consts of the module not used as class body
    used_as_class_body = {id_(c["name"]) for c in classes}
    for const in consts:
        if isinstance(const, types.CodeType) and const.co_name not in {"<module>", "<lambda>"}:
            # heuristic: if a class with same name exists, skip (it's the body)
            if any(c["name"] == const.co_name for c in classes):
                continue
            top_funcs.append((const.co_name, format_signature(const), first_docstring(const)))

    return top_funcs, classes


def id_(x):
    return x


def render_report(pyc: Path, code: types.CodeType) -> str:
    out = []
    out.append(f"# {pyc.name}")
    out.append("")
    out.append(f"_Python 3.11 bytecode — extracted via stdlib (no decompiler available)._")
    out.append("")

    doc = first_docstring(code)
    if doc:
        out.append("## Module docstring")
        out.append("")
        out.append("```")
        out.append(doc.strip())
        out.append("```")
        out.append("")

    imports = recover_imports(code)
    if imports:
        out.append("## Imports")
        out.append("")
        for imp in imports:
            out.append(f"- `{imp}`")
        out.append("")

    top_funcs, classes = collect_classes_and_funcs(code)

    if classes:
        out.append("## Classes")
        out.append("")
        for cls in classes:
            bases = f"({', '.join(cls['bases'])})" if cls["bases"] else ""
            out.append(f"### `class {cls['name']}{bases}`")
            if cls["doc"]:
                out.append(f"> {cls['doc'].strip().splitlines()[0]}")
            out.append("")
            if cls["methods"]:
                for name, sig, mdoc in cls["methods"]:
                    out.append(f"- `{name}{sig}`" + (f" — {mdoc.strip().splitlines()[0]}" if mdoc else ""))
            else:
                out.append("_(no methods recovered)_")
            out.append("")

    if top_funcs:
        out.append("## Top-level functions")
        out.append("")
        for name, sig, fdoc in top_funcs:
            out.append(f"- `{name}{sig}`" + (f" — {fdoc.strip().splitlines()[0]}" if fdoc else ""))
        out.append("")

    # String pool: useful for grepping later
    strings = sorted({
        c for code_obj in iter_codes(code)
        for c in code_obj.co_consts
        if isinstance(c, str) and len(c) >= 4 and "\n" not in c and not c.startswith("<")
    })
    if strings:
        out.append("## String constants (sample)")
        out.append("")
        out.append("```")
        for s in strings[:200]:
            out.append(s)
        if len(strings) > 200:
            out.append(f"... ({len(strings) - 200} more)")
        out.append("```")
        out.append("")

    # Disassembly of every named function
    out.append("## Bytecode disassembly")
    out.append("")
    for code_obj in iter_codes(code):
        if code_obj.co_name in {"<module>"}:
            continue
        out.append(f"### `{code_obj.co_qualname}`")
        out.append("")
        out.append("```")
        try:
            buf = []
            for ins in dis.get_instructions(code_obj):
                arg = "" if ins.argval is None else f"  {ins.argrepr or ins.argval!r}"
                buf.append(f"{ins.offset:>5}  {ins.opname:<24}{arg}")
            out.extend(buf[:300])
            if len(buf) > 300:
                out.append(f"... ({len(buf) - 300} more ops)")
        except Exception as e:
            out.append(f"# disassembly failed: {e}")
        out.append("```")
        out.append("")

    return "\n".join(out)


def process_one(pyc_path: Path, out_dir: Path) -> Path:
    code = load_code(pyc_path)
    text = render_report(pyc_path, code)
    out_path = out_dir / (pyc_path.stem + ".md")
    out_path.write_text(text, encoding="utf-8")
    return out_path


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    if args[0] == "--tree":
        root = Path(args[1])
        out_dir = Path(args[2]) if len(args) > 2 else root.parent / "decompiled"
        out_dir.mkdir(parents=True, exist_ok=True)
        for pyc in root.rglob("*.pyc"):
            if "__pycache__" in pyc.parts:
                continue
            rel = pyc.relative_to(root)
            target_dir = out_dir / rel.parent
            target_dir.mkdir(parents=True, exist_ok=True)
            try:
                code = load_code(pyc)
                text = render_report(pyc, code)
                (target_dir / (pyc.stem + ".md")).write_text(text, encoding="utf-8")
                print(f"[ok]  {rel}")
            except Exception as e:
                print(f"[err] {rel}: {e}")
    else:
        in_pyc = Path(args[0])
        out = Path(args[1]) if len(args) > 1 else in_pyc.with_suffix(".md")
        code = load_code(in_pyc)
        out.write_text(render_report(in_pyc, code), encoding="utf-8")
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
