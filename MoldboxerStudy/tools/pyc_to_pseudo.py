"""
pyc_to_pseudo.py — render a .pyc compiled with Python 3.11 as flat pseudo-Python.

This is NOT a real decompiler. It simulates the bytecode stack to recover
expressions (calls, attributes, comparisons, f-strings, containers) and emits
statements at points where the stack drains (STORE_*, RETURN_VALUE, POP_TOP).

Control flow is rendered as labels + explicit gotos rather than reconstructed
if/else/while — that keeps the converter simple and the output traceable.

For each function or class body we recurse into nested code objects and indent.

Usage:
  python pyc_to_pseudo.py <input.pyc> [output.py]
  python pyc_to_pseudo.py --tree <folder> <out_folder>
"""

from __future__ import annotations

import dis
import marshal
import struct
import sys
import types
from pathlib import Path


PYC_HEADER_LEN = 16


def load_code(pyc_path: Path) -> types.CodeType:
    raw = pyc_path.read_bytes()
    return marshal.loads(raw[PYC_HEADER_LEN:])


# ---------------------------------------------------------------------------
# Expression nodes (simple strings — we never need a real AST)
# ---------------------------------------------------------------------------


NULL_MARK = object()  # sentinel pushed by PUSH_NULL / LOAD_GLOBAL with NULL bit
KW_NAMES_MARK = "<KW_NAMES>"


def repr_const(c) -> str:
    if isinstance(c, types.CodeType):
        return f"<code:{c.co_qualname or c.co_name}>"
    if isinstance(c, frozenset):
        return "frozenset({" + ", ".join(repr_const(x) for x in sorted(c, key=repr)) + "})"
    if isinstance(c, tuple):
        return "(" + ", ".join(repr_const(x) for x in c) + ("," if len(c) == 1 else "") + ")"
    return repr(c)


COMPARE_OPS_TXT = {
    "<": "<", "<=": "<=", "==": "==", "!=": "!=", ">": ">", ">=": ">=",
}

BIN_OPS = {
    0: "+", 1: "&", 2: "//", 3: "<<", 4: "@", 5: "*", 6: "%", 7: "|",
    8: "**", 9: ">>", 10: "-", 11: "/", 12: "^",
    13: "+=", 14: "&=", 15: "//=", 16: "<<=", 17: "@=", 18: "*=",
    19: "%=", 20: "|=", 21: "**=", 22: ">>=", 23: "-=", 24: "/=", 25: "^=",
}


# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------


class Renderer:
    def __init__(self, code: types.CodeType, indent: int = 0):
        self.code = code
        self.indent = indent
        self.instructions = list(dis.get_instructions(code))
        # Map offset -> label number, if it's a jump target
        self.labels: dict[int, str] = {}
        self._collect_jump_targets()
        self.stack: list = []  # expression strings or NULL_MARK or KW_NAMES tuples
        self.lines: list[str] = []
        self.kw_names: tuple | None = None
        self.exception_depth = 0

    # -- pre-pass: assign labels to every jump target -------------------------
    def _collect_jump_targets(self):
        idx = 0
        for ins in self.instructions:
            if ins.is_jump_target:
                self.labels[ins.offset] = f"L{idx}"
                idx += 1

    # -- helpers --------------------------------------------------------------
    def emit(self, line: str):
        prefix = "    " * self.indent
        self.lines.append(prefix + line)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return "<EMPTY>"
        return self.stack.pop()

    def popn(self, n):
        if n == 0:
            return []
        out = self.stack[-n:]
        del self.stack[-n:]
        return out

    def _resolve_callable(self):
        """Pop the call target. Handles the (NULL + func) layout used by LOAD_GLOBAL
        with the 'push NULL' bit and PUSH_NULL/LOAD_METHOD."""
        target = self.pop()
        # Try to discard the NULL marker positioned just below the args we already
        # popped. If the next item is NULL_MARK, drop it.
        if self.stack and self.stack[-1] is NULL_MARK:
            self.stack.pop()
        return target

    # -- main loop ------------------------------------------------------------
    def render(self) -> list[str]:
        if self.labels.get(0):
            self.emit(f"# {self.labels[0]}:")
        for i, ins in enumerate(self.instructions):
            # Emit label if this offset is a jump target (other than 0 handled above)
            if ins.offset in self.labels and ins.offset != 0:
                # Flush dangling stack as a side-effect-free comment to keep state clean
                if self.stack:
                    self.emit(f"# (stack at label: {self.stack!r})")
                    self.stack.clear()
                self.emit(f"# {self.labels[ins.offset]}:")

            try:
                self._step(ins)
            except Exception as e:
                self.emit(f"# decompile error at offset {ins.offset} ({ins.opname}): {e}")
                self.stack.clear()
        # Render nested code objects (functions/classes) discovered along the way
        nested_blocks = []
        for const in self.code.co_consts:
            if isinstance(const, types.CodeType) and const.co_name not in {"<module>"}:
                nested_blocks.append(const)
        if nested_blocks:
            self.lines.append("")
            self.lines.append("    " * self.indent + "# --- nested code objects ---")
            for nested in nested_blocks:
                self.lines.append("")
                header = f"def {nested.co_qualname or nested.co_name}{format_signature(nested)}:"
                self.lines.append("    " * self.indent + header)
                sub = Renderer(nested, indent=self.indent + 1)
                self.lines.extend(sub.render())
        return self.lines

    # -- dispatch -------------------------------------------------------------
    def _step(self, ins):
        op = ins.opname
        arg = ins.argval
        argrepr = ins.argrepr

        # -- no-op-like
        if op in {"RESUME", "NOP", "PRECALL", "CACHE", "COPY_FREE_VARS", "MAKE_CELL", "PUSH_EXC_INFO", "SETUP_ANNOTATIONS", "EXTENDED_ARG"}:
            if op == "PUSH_EXC_INFO":
                self.emit("# (exception handler entry)")
                self.push("<exc_info>")
            return

        # -- loads
        if op == "LOAD_CONST":
            self.push(repr_const(arg))
            return
        if op == "LOAD_FAST" or op == "LOAD_NAME":
            self.push(arg)
            return
        if op == "LOAD_GLOBAL":
            # in 3.11, LOAD_GLOBAL may push NULL first if low bit set; argrepr shows "NULL + name"
            name = arg
            if isinstance(argrepr, str) and argrepr.startswith("NULL + "):
                self.push(NULL_MARK)
                name = argrepr[len("NULL + "):]
            self.push(name)
            return
        if op == "LOAD_DEREF":
            self.push(f"{arg}")  # closure cell name
            return
        if op == "LOAD_CLOSURE":
            self.push(f"<closure:{arg}>")
            return
        if op == "LOAD_ATTR":
            obj = self.pop()
            self.push(f"{obj}.{arg}")
            return
        if op == "LOAD_METHOD":
            obj = self.pop()
            # LOAD_METHOD pushes the method then NULL/self; we model as NULL + bound expr
            self.push(NULL_MARK)
            self.push(f"{obj}.{arg}")
            return
        if op == "LOAD_BUILD_CLASS":
            self.push("__build_class__")
            return
        if op == "PUSH_NULL":
            self.push(NULL_MARK)
            return
        if op == "LOAD_ASSERTION_ERROR":
            self.push("AssertionError")
            return

        # -- stores
        if op in {"STORE_FAST", "STORE_NAME", "STORE_GLOBAL"}:
            val = self.pop()
            self.emit(f"{arg} = {val}")
            return
        if op == "STORE_ATTR":
            obj = self.pop()
            val = self.pop()
            self.emit(f"{obj}.{arg} = {val}")
            return
        if op == "STORE_SUBSCR":
            idx = self.pop()
            obj = self.pop()
            val = self.pop()
            self.emit(f"{obj}[{idx}] = {val}")
            return
        if op == "STORE_DEREF":
            val = self.pop()
            self.emit(f"{arg} = {val}  # (cell)")
            return
        if op == "DELETE_FAST" or op == "DELETE_NAME" or op == "DELETE_GLOBAL":
            self.emit(f"del {arg}")
            return
        if op == "DELETE_SUBSCR":
            idx = self.pop()
            obj = self.pop()
            self.emit(f"del {obj}[{idx}]")
            return
        if op == "DELETE_ATTR":
            obj = self.pop()
            self.emit(f"del {obj}.{arg}")
            return

        # -- ops on top of stack
        if op == "BINARY_OP":
            b = self.pop()
            a = self.pop()
            sym = BIN_OPS.get(ins.arg, f"BIN({ins.arg})")
            self.push(f"({a} {sym} {b})")
            return
        if op == "BINARY_SUBSCR":
            idx = self.pop()
            obj = self.pop()
            self.push(f"{obj}[{idx}]")
            return
        if op == "COMPARE_OP":
            b = self.pop()
            a = self.pop()
            self.push(f"({a} {arg} {b})")
            return
        if op == "CONTAINS_OP":
            b = self.pop()
            a = self.pop()
            sym = "in" if ins.arg == 0 else "not in"
            self.push(f"({a} {sym} {b})")
            return
        if op == "IS_OP":
            b = self.pop()
            a = self.pop()
            sym = "is" if ins.arg == 0 else "is not"
            self.push(f"({a} {sym} {b})")
            return
        if op == "UNARY_NOT":
            a = self.pop()
            self.push(f"(not {a})")
            return
        if op == "UNARY_NEGATIVE":
            a = self.pop()
            self.push(f"(-{a})")
            return
        if op == "UNARY_INVERT":
            a = self.pop()
            self.push(f"(~{a})")
            return

        # -- containers
        if op == "BUILD_LIST":
            items = self.popn(ins.arg)
            self.push("[" + ", ".join(items) + "]")
            return
        if op == "BUILD_TUPLE":
            items = self.popn(ins.arg)
            joined = ", ".join(items)
            if ins.arg == 1:
                joined += ","
            self.push("(" + joined + ")")
            return
        if op == "BUILD_SET":
            items = self.popn(ins.arg)
            self.push("{" + ", ".join(items) + "}" if items else "set()")
            return
        if op == "BUILD_MAP":
            kv = self.popn(ins.arg * 2)
            pairs = [f"{kv[i]}: {kv[i + 1]}" for i in range(0, len(kv), 2)]
            self.push("{" + ", ".join(pairs) + "}")
            return
        if op == "BUILD_CONST_KEY_MAP":
            keys_repr = self.pop()  # already a tuple repr string like ('a', 'b', 'c')
            values = self.popn(ins.arg)
            # Try to parse the tuple repr back into individual key strings.
            keys = []
            try:
                inner = keys_repr.strip()
                if inner.startswith("(") and inner.endswith(")"):
                    inner = inner[1:-1]
                # Naive split — keys are typically string/number constants
                import ast as _ast
                parsed = _ast.literal_eval("(" + inner + (",)" if "," not in inner else ")"))
                if isinstance(parsed, tuple):
                    keys = [repr(k) for k in parsed]
                else:
                    keys = [repr(parsed)]
            except Exception:
                keys = [keys_repr]
            if len(keys) == len(values):
                pairs = [f"{k}: {v}" for k, v in zip(keys, values)]
                self.push("{" + ", ".join(pairs) + "}")
            else:
                self.push(f"<map keys={keys_repr} values={values}>")
            return
        if op == "LIST_EXTEND" or op == "LIST_APPEND":
            self.pop()
            return  # leave list on stack
        if op == "SET_UPDATE" or op == "SET_ADD":
            self.pop()
            return
        if op == "DICT_UPDATE" or op == "DICT_MERGE":
            self.pop()
            return
        if op == "LIST_TO_TUPLE":
            a = self.pop()
            self.push(f"tuple({a})")
            return

        # -- f-strings
        if op == "FORMAT_VALUE":
            # In 3.11, FORMAT_VALUE's arg encodes conversion + has-spec flags.
            # 0x01: !s, 0x02: !r, 0x03: !a, 0x04: format-spec follows on TOS.
            flag = ins.arg or 0
            spec = ""
            if flag & 0x04:
                spec_val = self.pop()
                if isinstance(spec_val, str) and spec_val.startswith("'") and spec_val.endswith("'"):
                    spec = ":" + spec_val.strip("'")
                else:
                    spec = f":{{{spec_val}}}"
            conv = ""
            if (flag & 0x03) == 0x01:
                conv = "!s"
            elif (flag & 0x03) == 0x02:
                conv = "!r"
            elif (flag & 0x03) == 0x03:
                conv = "!a"
            val = self.pop()
            self.push(f"<fpart {{{val}{conv}{spec}}}>")
            return
        if op == "BUILD_STRING":
            parts = self.popn(ins.arg)
            # Stitch <fpart {...}> tokens and string literals into a single f-string.
            pieces = []
            for p in parts:
                if isinstance(p, str) and p.startswith("<fpart "):
                    pieces.append(p[len("<fpart "):-1])
                elif isinstance(p, str) and p.startswith("'") and p.endswith("'"):
                    pieces.append(p[1:-1])
                elif isinstance(p, str) and p.startswith('"') and p.endswith('"'):
                    pieces.append(p[1:-1])
                else:
                    pieces.append(f"{{{p}}}")
            self.push("f'" + "".join(pieces) + "'")
            return

        # -- calls
        if op == "KW_NAMES":
            self.kw_names = arg  # tuple of names
            return
        if op == "CALL":
            n = ins.arg
            args = self.popn(n)
            kw_names = self.kw_names or ()
            self.kw_names = None
            n_kw = len(kw_names)
            n_pos = n - n_kw
            pos_args = args[:n_pos]
            kw_pairs = [f"{k}={v}" for k, v in zip(kw_names, args[n_pos:])]
            target = self._resolve_callable()
            call_expr = f"{target}({', '.join(pos_args + kw_pairs)})"
            self.push(call_expr)
            return
        if op == "CALL_FUNCTION_EX":
            # 0x01 flag: kwargs dict on top
            if ins.arg & 0x01:
                kwargs = self.pop()
                args = self.pop()
                target = self._resolve_callable()
                self.push(f"{target}(*{args}, **{kwargs})")
            else:
                args = self.pop()
                target = self._resolve_callable()
                self.push(f"{target}(*{args})")
            return

        # -- function/class creation
        if op == "MAKE_FUNCTION":
            code_obj_repr = self.pop()
            # MAKE_FUNCTION flags consume extras: 0x01 defaults, 0x02 kw_defaults, 0x04 annotations, 0x08 closure
            extras = []
            flags = ins.arg or 0
            if flags & 0x08:
                extras.append(f"closure={self.pop()}")
            if flags & 0x04:
                extras.append(f"annotations={self.pop()}")
            if flags & 0x02:
                extras.append(f"kw_defaults={self.pop()}")
            if flags & 0x01:
                extras.append(f"defaults={self.pop()}")
            extra = (" [" + ", ".join(extras) + "]") if extras else ""
            self.push(f"<function {code_obj_repr}{extra}>")
            return

        # -- iteration
        if op == "GET_ITER":
            a = self.pop()
            self.push(f"iter({a})")
            return
        if op == "FOR_ITER":
            iterable = self.stack[-1] if self.stack else "<iter>"
            target_off = ins.argval  # offset of exit
            target_label = self.labels.get(target_off, f"@{target_off}")
            self.emit(f"# for-iter from {iterable}: on StopIteration goto {target_label}")
            self.push("<for_iter_value>")
            return

        # -- control flow
        if op in {"JUMP_FORWARD", "JUMP_BACKWARD", "JUMP_BACKWARD_NO_INTERRUPT"}:
            target = ins.argval
            self.emit(f"goto {self.labels.get(target, f'@{target}')}")
            return
        if op.startswith("POP_JUMP"):
            cond = self.pop()
            target = ins.argval
            negate = "_IF_FALSE" in op or "_IF_NONE" in op
            keyword = "if not" if negate else "if"
            # Map specific variants for clarity
            if "_IF_NONE" in op:
                keyword = f"if {cond} is None"
                self.emit(f"{keyword}: goto {self.labels.get(target, f'@{target}')}")
                return
            if "_IF_NOT_NONE" in op:
                self.emit(f"if {cond} is not None: goto {self.labels.get(target, f'@{target}')}")
                return
            self.emit(f"{keyword} ({cond}): goto {self.labels.get(target, f'@{target}')}")
            return
        if op == "RETURN_VALUE":
            val = self.pop()
            self.emit(f"return {val}")
            return
        if op == "RETURN_CONST":
            self.emit(f"return {repr_const(arg)}")
            return
        if op == "YIELD_VALUE":
            val = self.pop()
            self.push(f"<yield {val}>")
            return
        if op == "RAISE_VARARGS":
            n = ins.arg or 0
            if n == 0:
                self.emit("raise")
            elif n == 1:
                self.emit(f"raise {self.pop()}")
            else:
                cause = self.pop()
                exc = self.pop()
                self.emit(f"raise {exc} from {cause}")
            return
        if op == "RERAISE":
            self.emit("raise  # (reraise)")
            return
        if op == "POP_EXCEPT":
            self.emit("# pop_except")
            return
        if op == "CHECK_EXC_MATCH":
            b = self.pop()
            a = self.stack[-1] if self.stack else "<exc>"
            self.push(f"isinstance({a}, {b})")
            return

        # -- stack management
        if op == "POP_TOP":
            if self.stack:
                expr = self.pop()
                if expr is NULL_MARK:
                    return
                self.emit(f"{expr}  # (discarded)")
            return
        if op == "COPY":
            n = ins.arg
            self.push(self.stack[-n])
            return
        if op == "SWAP":
            n = ins.arg
            self.stack[-1], self.stack[-n] = self.stack[-n], self.stack[-1]
            return
        if op == "DUP_TOP" or op == "DUP_TOP_TWO":
            self.push(self.stack[-1])
            return
        if op == "UNPACK_SEQUENCE":
            seq = self.pop()
            # push N placeholders that will be paired with subsequent STOREs in reverse
            for i in reversed(range(ins.arg)):
                self.push(f"{seq}[{i}]")
            return
        if op == "UNPACK_EX":
            # complicated — emit comment
            self.pop()
            for i in range(ins.arg + 1):
                self.push(f"<unpack_ex_{i}>")
            return

        # -- imports
        if op == "IMPORT_NAME":
            fromlist = self.pop()
            level = self.pop()
            self.emit(f"import {arg}  # level={level}, fromlist={fromlist}")
            self.push(f"<module:{arg}>")
            return
        if op == "IMPORT_FROM":
            mod = self.stack[-1]
            self.push(f"{mod}.{arg}")
            return
        if op == "IMPORT_STAR":
            self.emit(f"from {self.pop()} import *")
            return

        # -- with / context managers
        if op in {"BEFORE_WITH", "WITH_EXCEPT_START"}:
            self.emit(f"# {op}")
            return

        # -- send / async (probably unused in this codebase)
        if op in {"SEND", "GET_AWAITABLE", "GET_AITER", "GET_ANEXT", "END_ASYNC_FOR"}:
            self.emit(f"# {op}")
            return

        # -- fallback
        self.emit(f"# UNHANDLED {op} arg={ins.arg!r} argval={arg!r}")


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
    has_varargs = bool(code.co_flags & 0x04)
    has_kwargs = bool(code.co_flags & 0x08)
    if has_varargs:
        parts.append(f"*{varnames[argcount + kwonly]}")
    elif kwonlies:
        parts.append("*")
    parts.extend(kwonlies)
    if has_kwargs:
        rest_idx = argcount + kwonly + (1 if has_varargs else 0)
        parts.append(f"**{varnames[rest_idx]}")
    return f"({', '.join(parts)})"


def render_module(pyc: Path, code: types.CodeType) -> str:
    header = [
        f"# Pseudo-Python reconstructed from {pyc.name}",
        f"# Original source path (from bytecode): {code.co_filename}",
        f"# NOT executable — control flow uses labels + gotos.",
        "",
    ]
    body = Renderer(code).render()
    return "\n".join(header + body)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    if args[0] == "--tree":
        root = Path(args[1])
        out_dir = Path(args[2])
        out_dir.mkdir(parents=True, exist_ok=True)
        for pyc in root.rglob("*.pyc"):
            if "__pycache__" in pyc.parts:
                continue
            rel = pyc.relative_to(root)
            target_dir = out_dir / rel.parent
            target_dir.mkdir(parents=True, exist_ok=True)
            try:
                code = load_code(pyc)
                text = render_module(pyc, code)
                (target_dir / (pyc.stem + ".py")).write_text(text, encoding="utf-8")
                print(f"[ok]  {rel}")
            except Exception as e:
                print(f"[err] {rel}: {e}")
    else:
        in_pyc = Path(args[0])
        out = Path(args[1]) if len(args) > 1 else in_pyc.with_suffix(".py")
        code = load_code(in_pyc)
        out.write_text(render_module(in_pyc, code), encoding="utf-8")
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
