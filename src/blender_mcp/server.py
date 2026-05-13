# blender_mcp_server.py
from mcp.server.fastmcp import FastMCP, Context, Image
import socket
import json
import asyncio
import logging
import tempfile
from dataclasses import dataclass
from contextlib import asynccontextmanager
from typing import AsyncIterator, Dict, Any
import os

# Import telemetry
from .telemetry import record_startup, get_telemetry
from .telemetry_decorator import telemetry_tool

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("BlenderMCPServer")

# Default configuration
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 9876

@dataclass
class BlenderConnection:
    host: str
    port: int
    sock: socket.socket = None

    def connect(self) -> bool:
        if self.sock:
            return True
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            logger.info(f"Connected to Blender at {self.host}:{self.port}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Blender: {str(e)}")
            self.sock = None
            return False

    def disconnect(self):
        if self.sock:
            try:
                self.sock.close()
            except Exception as e:
                logger.error(f"Error disconnecting from Blender: {str(e)}")
            finally:
                self.sock = None

    def receive_full_response(self, sock, buffer_size=8192):
        chunks = []
        sock.settimeout(180.0)
        try:
            while True:
                try:
                    chunk = sock.recv(buffer_size)
                    if not chunk:
                        if not chunks:
                            raise Exception("Connection closed before receiving any data")
                        break
                    chunks.append(chunk)
                    try:
                        data = b''.join(chunks)
                        json.loads(data.decode('utf-8'))
                        logger.info(f"Received complete response ({len(data)} bytes)")
                        return data
                    except json.JSONDecodeError:
                        continue
                except socket.timeout:
                    logger.warning("Socket timeout during chunked receive")
                    break
                except (ConnectionError, BrokenPipeError, ConnectionResetError) as e:
                    logger.error(f"Socket connection error during receive: {str(e)}")
                    raise
        except socket.timeout:
            logger.warning("Socket timeout during chunked receive")
        except Exception as e:
            logger.error(f"Error during receive: {str(e)}")
            raise

        if chunks:
            data = b''.join(chunks)
            logger.info(f"Returning data after receive completion ({len(data)} bytes)")
            try:
                json.loads(data.decode('utf-8'))
                return data
            except json.JSONDecodeError:
                raise Exception("Incomplete JSON response received")
        else:
            raise Exception("No data received")

    def send_command(self, command_type: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        if not self.sock and not self.connect():
            raise ConnectionError("Not connected to Blender")

        command = {"type": command_type, "params": params or {}}

        try:
            logger.info(f"Sending command: {command_type} with params: {params}")
            self.sock.sendall(json.dumps(command).encode('utf-8'))
            logger.info(f"Command sent, waiting for response...")
            self.sock.settimeout(180.0)
            response_data = self.receive_full_response(self.sock)
            logger.info(f"Received {len(response_data)} bytes of data")
            response = json.loads(response_data.decode('utf-8'))
            logger.info(f"Response parsed, status: {response.get('status', 'unknown')}")

            if response.get("status") == "error":
                logger.error(f"Blender error: {response.get('message')}")
                raise Exception(response.get("message", "Unknown error from Blender"))

            return response.get("result", {})
        except socket.timeout:
            logger.error("Socket timeout while waiting for response from Blender")
            self.sock = None
            raise Exception("Timeout waiting for Blender response - try simplifying your request")
        except (ConnectionError, BrokenPipeError, ConnectionResetError) as e:
            logger.error(f"Socket connection error: {str(e)}")
            self.sock = None
            raise Exception(f"Connection to Blender lost: {str(e)}")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON response from Blender: {str(e)}")
            if 'response_data' in locals() and response_data:
                logger.error(f"Raw response (first 200 bytes): {response_data[:200]}")
            raise Exception(f"Invalid response from Blender: {str(e)}")
        except Exception as e:
            logger.error(f"Error communicating with Blender: {str(e)}")
            self.sock = None
            raise Exception(f"Communication error with Blender: {str(e)}")

@asynccontextmanager
async def server_lifespan(server: FastMCP) -> AsyncIterator[Dict[str, Any]]:
    try:
        logger.info("BlenderMCP server starting up")

        try:
            record_startup()
        except Exception as e:
            logger.debug(f"Failed to record startup telemetry: {e}")

        try:
            blender = get_blender_connection()
            logger.info("Successfully connected to Blender on startup")
        except Exception as e:
            logger.warning(f"Could not connect to Blender on startup: {str(e)}")
            logger.warning("Make sure the Blender addon is running before using Blender resources or tools")

        yield {}
    finally:
        global _blender_connection
        if _blender_connection:
            logger.info("Disconnecting from Blender on shutdown")
            _blender_connection.disconnect()
            _blender_connection = None
        logger.info("BlenderMCP server shut down")

mcp = FastMCP("BlenderMCP", lifespan=server_lifespan)

_blender_connection = None

def get_blender_connection():
    global _blender_connection

    if _blender_connection is not None:
        try:
            _blender_connection.send_command("ping")
            return _blender_connection
        except Exception as e:
            logger.warning(f"Existing connection is no longer valid: {str(e)}")
            try:
                _blender_connection.disconnect()
            except:
                pass
            _blender_connection = None

    if _blender_connection is None:
        host = os.getenv("BLENDER_HOST", DEFAULT_HOST)
        port = int(os.getenv("BLENDER_PORT", DEFAULT_PORT))
        _blender_connection = BlenderConnection(host=host, port=port)
        if not _blender_connection.connect():
            logger.error("Failed to connect to Blender")
            _blender_connection = None
            raise Exception("Could not connect to Blender. Make sure the Blender addon is running.")
        logger.info("Created new persistent connection to Blender")

    return _blender_connection


@telemetry_tool("get_scene_info")
@mcp.tool()
def get_scene_info(ctx: Context) -> str:
    """Get detailed information about the current Blender scene."""
    try:
        blender = get_blender_connection()
        result = blender.send_command("get_scene_info")
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error getting scene info from Blender: {str(e)}")
        return f"Error getting scene info: {str(e)}"

@telemetry_tool("get_object_info")
@mcp.tool()
def get_object_info(ctx: Context, object_name: str) -> str:
    """
    Get detailed information about a specific object in the Blender scene.

    Parameters:
    - object_name: The name of the object to get information about
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("get_object_info", {"name": object_name})
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error getting object info from Blender: {str(e)}")
        return f"Error getting object info: {str(e)}"

@telemetry_tool("get_viewport_screenshot")
@mcp.tool()
def get_viewport_screenshot(ctx: Context, max_size: int = 800) -> Image:
    """
    Capture a screenshot of the current Blender 3D viewport.

    Parameters:
    - max_size: Maximum size in pixels for the largest dimension (default: 800)
    """
    try:
        blender = get_blender_connection()
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, f"blender_screenshot_{os.getpid()}.png")

        result = blender.send_command("get_viewport_screenshot", {
            "max_size": max_size,
            "filepath": temp_path,
            "format": "png"
        })

        if "error" in result:
            raise Exception(result["error"])
        if not os.path.exists(temp_path):
            raise Exception("Screenshot file was not created")

        with open(temp_path, 'rb') as f:
            image_bytes = f.read()
        os.remove(temp_path)

        return Image(data=image_bytes, format="png")
    except Exception as e:
        logger.error(f"Error capturing screenshot: {str(e)}")
        raise Exception(f"Screenshot failed: {str(e)}")


@telemetry_tool("execute_blender_code")
@mcp.tool()
def execute_blender_code(ctx: Context, code: str) -> str:
    """
    Execute arbitrary Python code in Blender. Break complex operations into smaller chunks.

    Parameters:
    - code: The Python code to execute
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("execute_code", {"code": code})
        return f"Code executed successfully: {result.get('result', '')}"
    except Exception as e:
        logger.error(f"Error executing code: {str(e)}")
        return f"Error executing code: {str(e)}"


@telemetry_tool("import_stl")
@mcp.tool()
def import_stl(ctx: Context, filepath: str, object_name: str = None) -> str:
    """
    Import an STL file into the current Blender scene. Use this as the first step
    of any print-prep pipeline.

    Parameters:
    - filepath: Absolute path to the .stl file on disk.
    - object_name: Optional. Rename the imported object to this name (otherwise
      Blender derives it from the filename).

    Returns JSON with imported object name, vertex/edge/face count, dimensions in
    millimeters (assuming Blender units == meters, the default), and bounding box.
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("import_stl", {
            "filepath": filepath,
            "object_name": object_name,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error importing STL: {str(e)}")
        return f"Error importing STL: {str(e)}"


@telemetry_tool("export_stl")
@mcp.tool()
def export_stl(
    ctx: Context,
    object_name: str,
    filepath: str,
    apply_modifiers: bool = True,
) -> str:
    """
    Export a single object as an STL file, ready to feed to a slicer.

    Parameters:
    - object_name: Name of the object to export.
    - filepath: Absolute path for the output .stl file (will be overwritten).
    - apply_modifiers: If True, modifiers are baked into the exported geometry
      (default and recommended for print-ready output).

    Returns JSON with the written filepath and final triangle count.
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("export_stl", {
            "object_name": object_name,
            "filepath": filepath,
            "apply_modifiers": apply_modifiers,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error exporting STL: {str(e)}")
        return f"Error exporting STL: {str(e)}"


@telemetry_tool("analyze_mesh_for_print")
@mcp.tool()
def analyze_mesh_for_print(ctx: Context, object_name: str) -> str:
    """
    Run a structured print-readiness check on a mesh and return JSON.

    The MCP assistant cannot see the viewport. This tool is its primary "eye":
    it returns a structured JSON describing the mesh state in numbers, so the
    assistant can reason about cleanup decisions without rendering.

    Returns (all units in mm; counts are integers; ratios are floats):
      Topology:
        vertex_count, edge_count, face_count
        non_manifold_edges, boundary_edges, boundary_loops
        disconnected_shells
        degenerate_faces (area < 1e-12 m²)
        watertight (bool: non_manifold_edges == 0)
        normals: "consistent" | "all_inverted" | "unknown_open_mesh"
        signed_volume_mm3
        ready_to_slice (bool: watertight AND no degenerate AND shells==1 AND normals consistent)
      Dimensions:
        dimensions_mm [x, y, z]
        surface_area_mm2
        center_of_mass_mm [x, y, z]  (area-weighted surface centroid)
      Wall thickness (watertight only, raycast-sampled, capped at 5000 faces):
        wall_thickness_p10_mm, wall_thickness_p50_mm
        wall_thickness_under_min_pct  (% faces below 0.8mm)
      Normals statistics (watertight only):
        inverted_face_pct  (0..100; raycast-sampled; partial inversion detect)
      Geometric quality (proxies for visual inspection):
        aspect_ratio_p95  (95p of max/min edge length ratio per face;
                           >10 = sliver triangles, typically post-decimate)
        dihedral_angle_p90_deg  (90p of dihedral angle across manifold edges;
                                 >60 = visible sharp folds)
        bottom_contact_area_mm2  (area of faces facing downward, normal.z <= -0.95;
                                  proxy for build-plate adhesion)
        convex_hull_volume_ratio  (volume / hull_volume in (0,1]; 1=brick,
                                   <0.5=thin/spiky, blob-vs-spiky proxy)

    These numeric proxies replace common visual checks the assistant cannot do:
      - "Are there sliver triangles?" -> aspect_ratio_p95 > 10
      - "Will it sit stable on the plate?" -> bottom_contact_area_mm2 vs
        dimensions_mm[0] * dimensions_mm[1]
      - "Is the part spiky or chunky?" -> convex_hull_volume_ratio
      - "How heavy/expensive in PLA?" -> surface_area_mm2 (shell volume estimate)
      - "Will it tip during print?" -> compare center_of_mass_mm[0:2] with the
        bbox of bottom_contact faces

    Use this BEFORE running cleanup ops (so you know what to fix) and AFTER
    (so you know it's done). Feed the JSON directly into kb_route(analysis_json)
    to get the next action.

    Parameters:
    - object_name: Name of the mesh object to analyze.
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("analyze_mesh_for_print", {
            "object_name": object_name,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error analyzing mesh: {str(e)}")
        return f"Error analyzing mesh: {str(e)}"


@telemetry_tool("analyze_overhang")
@mcp.tool()
def analyze_overhang(ctx: Context, object_name: str) -> str:
    """
    R25 TESTING_LOG: ritorna metriche overhang e decision tree raccomandata per supporti.

    NON tocca la mesh. Usalo PRIMA di consigliare "Support: Off" — mai dare la
    decisione per intuito (regola 25 docs/membrane_removal.md).

    Returns JSON con:
      overhang_45_pct: % area facce con normal.z < cos(45°) sopra il bed
      quasi_flat_ceiling_pct: % area facce con normal.z < -0.97 (quasi piatto)
      support_decision: "OFF" | "Auto threshold 45°" | "ON Tree Hybrid OBBLIGATORIO"
      reasoning: spiegazione della scelta

    Decision tree:
      pct_45 < 3% AND pct_flat < 1% → OFF
      pct_45 < 10%                   → Auto Normal
      pct_45 >= 10%                  → Tree Hybrid OBBLIGATORIO

    Parameters:
    - object_name: Name of the mesh object to analyze.
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("analyze_overhang", {"object_name": object_name})
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error analyzing overhang: {str(e)}")
        return f"Error analyzing overhang: {str(e)}"


@telemetry_tool("check_pre_export")
@mcp.tool()
def check_pre_export(
    ctx: Context,
    object_name: str,
    expected_contact_points: int = 1,
    z_tolerance_mm: float = 0.5,
) -> str:
    """
    R36 TESTING_LOG: verifica pre-export OBBLIGATORIA prima di wm.stl_export.

    Conferma che:
    - bbox_z_min == 0 (asset allineato al bed)
    - contact_points_count >= expected_contact_points
      (= N "piedi" che effettivamente toccano il bed entro z_tolerance_mm)
    - mesh è manifold (non_manifold_edges == 0, boundary == 0)

    Caso animale 4 zampe: passa expected_contact_points=4. Caso vaso/base
    singola: 1.

    Returns JSON con flag ready_to_export + warnings list.

    Parameters:
    - object_name: Name of the mesh object to check.
    - expected_contact_points: int, atteso N punti di appoggio (default 1).
    - z_tolerance_mm: float, tolleranza in mm per considerare un vertice "in contatto"
      con il bed (default 0.5).
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("check_pre_export", {
            "object_name": object_name,
            "expected_contact_points": expected_contact_points,
            "z_tolerance_mm": z_tolerance_mm,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error in check_pre_export: {str(e)}")
        return f"Error in check_pre_export: {str(e)}"


@telemetry_tool("render_hires_multiview")
@mcp.tool()
def render_hires_multiview(
    ctx: Context,
    object_name: str,
    views: str = "TOP,BOTTOM,FRONT",
    resolution_x: int = 1920,
    resolution_y: int = 1440,
    output_dir: str = "",
) -> str:
    """
    R30 TESTING_LOG: render OpenGL HIRES multi-vista per validazione visiva.

    Le viste vanno sempre validate ad ALTA risoluzione (1920×1440+) da angolazioni
    multiple: i render bassi nascondono difetti e portano a falsi positivi
    "operazione completata" (caso documentato 5+ volte in SESSION 004).

    Parameters:
    - object_name: Name of the mesh object to render.
    - views: comma-separated list, valid values: TOP/BOTTOM/FRONT/BACK/LEFT/RIGHT.
      Default: "TOP,BOTTOM,FRONT".
    - resolution_x, resolution_y: pixel (default 1920×1440).
    - output_dir: cartella output (default tempdir di sistema).
      Suggerito: r"C:\\Users\\<user>\\Desktop\\Bambu\\<progetto>\\screen_mcp"
    """
    try:
        view_list = [v.strip().upper() for v in views.split(",") if v.strip()]
        blender = get_blender_connection()
        params = {
            "object_name": object_name,
            "views": view_list,
            "resolution_x": resolution_x,
            "resolution_y": resolution_y,
        }
        if output_dir:
            params["output_dir"] = output_dir
        result = blender.send_command("render_hires_multiview", params)
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error in render_hires_multiview: {str(e)}")
        return f"Error in render_hires_multiview: {str(e)}"


@telemetry_tool("compute_face_visibility_bvh")
@mcp.tool()
def compute_face_visibility_bvh(
    ctx: Context,
    object_name: str,
    n_rays: int = 32,
    vis_threshold: float = 0.10,
    ray_distance: float = 10.0,
) -> str:
    """
    R38 TESTING_LOG: identifica facce interne (= non visibili dall'esterno) via
    BVHTree raycast Fibonacci hemisphere. NON cancella nulla, ritorna SOLO la
    lista degli indici delle facce candidate alla rimozione.

    Per ogni faccia, casta `n_rays` raggi su semisfera lungo la normale. Se
    `< vis_threshold` frazione di raggi escono dal mesh entro `ray_distance`, la
    faccia è classificata "interna".

    Usalo per asset sculpt con membrane interne integrate (alberi corallo,
    gabbie). PRIMA di tentare verifica con regola 41 che la tela NON sia
    intenzionale (filename contiene `relief|wall_art|2.5D|plaque|medallion|lithophane`).

    Performance: ~30-90s su 250k tri.

    Parameters:
    - object_name: Name of the mesh object.
    - n_rays: int, raggi per faccia (16=rapido, 32=bilanciato, 64=preciso).
    - vis_threshold: float 0..1, soglia visibilità (0.10 aggressivo, 0.30 conservativo).
    - ray_distance: float, lunghezza massima ray in unità Blender (10.0 default).

    Returns JSON con interior_face_indices (lista int), interior_face_pct, params.
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("compute_face_visibility_bvh", {
            "object_name": object_name,
            "n_rays": n_rays,
            "vis_threshold": vis_threshold,
            "ray_distance": ray_distance,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error in compute_face_visibility_bvh: {str(e)}")
        return f"Error in compute_face_visibility_bvh: {str(e)}"


@telemetry_tool("compute_ao_per_vertex_pymeshlab")
@mcp.tool()
def compute_ao_per_vertex_pymeshlab(
    ctx: Context,
    input_stl_path: str,
    output_stl_path: str,
    ao_threshold: float = 0.15,
    reqviews: int = 128,
    use_gpu: bool = True,
) -> str:
    """
    R37 TESTING_LOG: rimozione membrana interna via PyMeshLab Ambient Occlusion
    per-vertex. Opera FUORI Blender via PyMeshLab (libreria standalone).

    Bake AO sui vertici → la membrana interna è "in ombra" (vertici scuri),
    i dettagli esterni "visibili" (vertici chiari). Cancella facce con TUTTI
    i 3 vertici sotto soglia ao_threshold.

    Workflow: salva STL da Blender → questo tool → re-importa output STL.

    Parameters:
    - input_stl_path: Path STL input (export precedentemente da Blender).
    - output_stl_path: Path STL output con membrana rimossa.
    - ao_threshold: 0..1, soglia AO sotto la quale i vertici sono "in ombra"
      (0.10-0.15 conservativo, 0.05 aggressivo). Default 0.15.
    - reqviews: int, numero raggi AO sphere (128 bilanciato, 256+ preciso).
    - use_gpu: bool, usa GPU acceleration se disponibile (richiede driver OpenGL).

    Returns JSON con esito + stats.
    """
    try:
        # Esecuzione standalone via pymeshlab — NON serve Blender bridge
        import pymeshlab
        ms = pymeshlab.MeshSet()
        ms.load_new_mesh(input_stl_path)
        v_before = ms.current_mesh().vertex_number()
        f_before = ms.current_mesh().face_number()

        # Bake AO per-vertex
        if use_gpu:
            try:
                ms.compute_scalar_ambient_occlusion_gpu(
                    occmode='per-Vertex',
                    dirbias=0,
                    reqviews=reqviews,
                )
            except Exception:
                # Fallback CPU
                ms.compute_scalar_ambient_occlusion(
                    occmode='per-Vertex',
                    dirbias=0,
                    reqviews=reqviews,
                )
        else:
            ms.compute_scalar_ambient_occlusion(
                occmode='per-Vertex',
                dirbias=0,
                reqviews=reqviews,
            )

        # Seleziona + delete facce con tutti i vertici sotto soglia
        cond = f"(q0 < {ao_threshold}) && (q1 < {ao_threshold}) && (q2 < {ao_threshold})"
        ms.compute_selection_by_condition_per_face(condselect=cond)
        ms.meshing_remove_selected_faces()
        ms.meshing_remove_unreferenced_vertices()

        ms.save_current_mesh(output_stl_path)
        v_after = ms.current_mesh().vertex_number()
        f_after = ms.current_mesh().face_number()

        return json.dumps({
            "input_stl": input_stl_path,
            "output_stl": output_stl_path,
            "vertex_count_before": v_before,
            "vertex_count_after": v_after,
            "face_count_before": f_before,
            "face_count_after": f_after,
            "faces_removed": f_before - f_after,
            "faces_removed_pct": round(100.0 * (f_before - f_after) / f_before, 1) if f_before > 0 else 0,
            "ao_threshold": ao_threshold,
            "reqviews": reqviews,
            "use_gpu": use_gpu,
        }, indent=2)
    except ImportError:
        return "Error: pymeshlab not installed. Run: cd <repo> && uv add pymeshlab"
    except Exception as e:
        logger.error(f"Error in compute_ao_per_vertex_pymeshlab: {str(e)}")
        return f"Error in compute_ao_per_vertex_pymeshlab: {str(e)}"


# ---------------------------------------------------------------------------
# Moldboxer integration tools
#
# Six MCP tools that wrap the `moldboxer_lite` reconstruction library
# (study + replica of the commercial Moldboxer 1.4.9 silicone-mold add-on).
# All geometry runs inside Blender via the addon handler; this side just
# forwards JSON. See MoldboxerStudy/CLAUDE.md for the full architecture.
# ---------------------------------------------------------------------------


@telemetry_tool("mb_setup_mm")
@mcp.tool()
def mb_setup_mm(ctx: Context) -> str:
    """
    Configure the active Blender scene to use millimeter units.

    Call this ONCE at the very start of a Moldboxer pipeline so that distances
    (gap, channel width/depth, key size, …) in the other mb_* tools are
    interpreted as mm.

    No parameters. Returns JSON with {"ok": true, "unit": "MILLIMETERS"}.
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("mb_setup_mm", {})
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error in mb_setup_mm: {str(e)}")
        return f"Error in mb_setup_mm: {str(e)}"


@telemetry_tool("mb_preprocess_patron")
@mcp.tool()
def mb_preprocess_patron(
    ctx: Context,
    object_name: str = None,
    master_quality: str = "HIGH",
    center: bool = True,
    isolate: bool = False,
) -> str:
    """
    Preprocess the imported master mesh as the `patron` for a mold pipeline.

    Renames the target object to 'patron', applies transforms, optionally
    snaps it to the origin (Z=0 at the bottom), and runs a voxel heal pass
    if the mesh is non-manifold.

    Call this AFTER mb_setup_mm and AFTER importing the STL (e.g. via
    `import_stl`). Without this step the auto_box / auto_flat tools may
    fail because they expect a clean, centered, manifold patron at Z=0.

    Parameters:
    - object_name: Name of the object to preprocess. If None, uses the active
      object in the scene.
    - master_quality: "FAST" | "MID" | "HIGH" | "ULTRA". Controls voxel
      detail for the heal pass (HIGH is the Moldboxer default).
    - center: If True, snap XY to origin and put the bottom at Z=0.
    - isolate: If True, join disconnected sub-meshes (filtered by volume).

    Returns JSON with the patron summary (dimensions_mm, bbox).
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("mb_preprocess_patron", {
            "object_name": object_name,
            "master_quality": master_quality,
            "center": center,
            "isolate": isolate,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error in mb_preprocess_patron: {str(e)}")
        return f"Error in mb_preprocess_patron: {str(e)}"


@telemetry_tool("mb_auto_box")
@mcp.tool()
def mb_auto_box(
    ctx: Context,
    patron_name: str = "patron",
    box_gap: float = 4.5,
    box_quality: str = "MID",
    channel_width: float = 5.0,
    channel_depth: float = 6.0,
    adjust_to_contour: bool = True,
    larger_back: bool = True,
    funneler: bool = True,
    safe_mode: bool = False,
) -> str:
    """
    Generate a 2-part silicone mold box around the preprocessed patron.

    Client-side replica of Moldboxer's `silicone.auto_box` (replaces the
    POST /auto-box/ server call). Builds a voxel-wrapped offset hull, adds
    side channels for clamps, a funneler/deposit on top, then carves the
    inner cavity by subtracting the patron.

    Call AFTER mb_preprocess_patron. Call mb_confirm_mold AFTER this to
    split the box on Y, add the base + volume text + interlock keys.

    Parameters:
    - patron_name: Name of the patron object (default "patron").
    - box_gap: Silicone thickness in mm (Moldboxer default 4.5).
    - box_quality: "FAST" | "MID" | "HIGH" | "ULTRA" (voxel detail).
    - channel_width, channel_depth: Channel size in mm.
    - adjust_to_contour: Snap channels to the master contour (currently
      uniform spacing in moldboxer_lite — may differ from the server).
    - larger_back: Use a larger radius for the back channel.
    - funneler: Add a top funneler/deposit for casting.
    - safe_mode: Build the wrapper from a sphere fallback (slower, safer).

    Returns JSON with the 'box' object summary (name, dimensions, bbox).
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("mb_auto_box", {
            "patron_name": patron_name,
            "box_gap": box_gap,
            "box_quality": box_quality,
            "channel_width": channel_width,
            "channel_depth": channel_depth,
            "adjust_to_contour": adjust_to_contour,
            "larger_back": larger_back,
            "funneler": funneler,
            "safe_mode": safe_mode,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error in mb_auto_box: {str(e)}")
        return f"Error in mb_auto_box: {str(e)}"


@telemetry_tool("mb_auto_flat")
@mcp.tool()
def mb_auto_flat(
    ctx: Context,
    patron_name: str = "patron",
    box_gap: float = 4.5,
    box_quality: str = "MID",
    grip_height: float = 10.0,
    open_top_margin: float = 2.0,
    add_volume_text: bool = False,
) -> str:
    """
    Generate a 1-piece, open-top silicone mold with a side grip ("Flat
    Automatic Box" in Moldboxer terms).

    Suitable for short or flat masters that demold by pulling the silicone
    straight up. Not suitable for masters with overhangs/undercuts — use
    mb_auto_box for those.

    Call AFTER mb_preprocess_patron. No mb_confirm_mold needed afterwards
    (flat molds are single-piece).

    Parameters:
    - patron_name: Name of the patron object (default "patron").
    - box_gap: Silicone thickness in mm (Moldboxer default 4.5).
    - box_quality: "FAST" | "MID" | "HIGH" | "ULTRA".
    - grip_height: Side grip cube edge length in mm.
    - open_top_margin: How much of the top is cut to leave the cavity open.
    - add_volume_text: Stamp the silicone volume in ml on the side.

    Returns JSON with the 'box' object summary.
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("mb_auto_flat", {
            "patron_name": patron_name,
            "box_gap": box_gap,
            "box_quality": box_quality,
            "grip_height": grip_height,
            "open_top_margin": open_top_margin,
            "add_volume_text": add_volume_text,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error in mb_auto_flat: {str(e)}")
        return f"Error in mb_auto_flat: {str(e)}"


@telemetry_tool("mb_confirm_mold")
@mcp.tool()
def mb_confirm_mold(
    ctx: Context,
    patron_name: str = "patron",
    box_name: str = "box",
    join_patron: bool = True,
    master_base_pin: bool = True,
    n_splits: int = 2,
    add_keys: bool = True,
    key_count: int = 4,
    key_size: float = 4.0,
    key_tolerance: float = 0.2,
    voxel_size: float = 0.8,
    space_objects: bool = True,
) -> str:
    """
    Finalize a 2-part mold built by mb_auto_box: compute silicone volume,
    add the base + wing + volume text, split on Y, add interlock keys.

    Client-side replica of Moldboxer's `silicone.confirm` (replaces the
    POST /confirm-silicone-mold/ server call).

    Parameters:
    - patron_name, box_name: Object names from earlier steps.
    - join_patron: "Fixed Master" mode — master and base merge into a single
      part. Use this for casting workflows where the master stays embedded.
    - master_base_pin: Add a centering pin under the master (only when
      join_patron is False).
    - n_splits: 0 (keep single box, no split) or 2 (split on Y).
    - add_keys: Add interlock keys on the split faces.
    - key_count, key_size, key_tolerance: Key shape params in mm.
    - voxel_size: Final cleanup voxel in mm.
    - space_objects: Spread {patron, mold, silicone_preview} along X for
      visual inspection (matches the original Moldboxer behaviour).

    Returns JSON with all output object names + silicone volume in mm³.
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("mb_confirm_mold", {
            "patron_name": patron_name,
            "box_name": box_name,
            "join_patron": join_patron,
            "master_base_pin": master_base_pin,
            "n_splits": n_splits,
            "add_keys": add_keys,
            "key_count": key_count,
            "key_size": key_size,
            "key_tolerance": key_tolerance,
            "voxel_size": voxel_size,
            "space_objects": space_objects,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error in mb_confirm_mold: {str(e)}")
        return f"Error in mb_confirm_mold: {str(e)}"


@telemetry_tool("mb_export_parts")
@mcp.tool()
def mb_export_parts(
    ctx: Context,
    dir_path: str,
    apply_modifiers: bool = True,
) -> str:
    """
    Export every mesh in the scene as STL into `dir_path`.

    File naming follows the Moldboxer convention:
      - objects containing 'patron' or 'silicone' → `<name>_<volume_ml>ml.stl`
      - other objects → `<name>.stl`

    Call this LAST in a Moldboxer pipeline. The directory is created if it
    doesn't exist.

    Parameters:
    - dir_path: Output directory (absolute path).
    - apply_modifiers: Bake modifiers into the exported geometry (recommended).

    Returns JSON with the count and list of files written.
    """
    try:
        blender = get_blender_connection()
        result = blender.send_command("mb_export_parts", {
            "dir_path": dir_path,
            "apply_modifiers": apply_modifiers,
        })
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error in mb_export_parts: {str(e)}")
        return f"Error in mb_export_parts: {str(e)}"


@mcp.prompt()
def mold_strategy() -> str:
    """Defines the preferred strategy for generating a silicone mold from a 3D master model."""
    return """Your job: take a 3D master model (STL or already-loaded mesh) and
generate a silicone mold ready to be 3D-printed in rigid material (PLA / resin),
filled with silicone, and used to cast copies of the master in soft material.

This is the Moldboxer-style pipeline, reconstructed client-side. You will not
call any external server; all geometry runs locally in Blender via the mb_* tools.

DECISION TREE - which mold style?

| Master shape | Tool | Notes |
|---|---|---|
| 3D with depth, full sculpt | mb_auto_box | 2-half mold split on Y. Default for figurines, busts. |
| Flat / shallow relief / 2.5D | mb_auto_flat | 1-piece, open-top with side grip. Demold by pulling. |
| Has overhangs / undercuts | mb_auto_box | Flat won't release. Box may need clear_extraction (not yet implemented). |

WORKFLOW (mb_auto_box, the common case):

1. mb_setup_mm()
   Configure scene units to millimeters. Always first.

2. import_stl(filepath=<absolute path to master.stl>)
   Or use the already-active object if the user pre-loaded the master.

3. mb_preprocess_patron(object_name=<name from step 2>,
                       master_quality="HIGH", center=True)
   Renames to 'patron', applies transforms, centers (Z=0 at bottom),
   voxel-heals if non-manifold.

4. mb_auto_box(patron_name="patron",
              box_gap=4.5,             # silicone thickness in mm
              box_quality="MID",
              channel_width=5.0,
              channel_depth=6.0,
              funneler=True)
   Builds box wrapper + channels + funneler + carves cavity.
   Inspect the result via get_viewport_screenshot() BEFORE confirming.

5. mb_confirm_mold(patron_name="patron", box_name="box",
                  n_splits=2, add_keys=True, key_count=4)
   Splits on Y, adds base + volume text + interlock keys.
   Returns volume_mm3 so the user knows how much silicone to buy.

6. mb_export_parts(dir_path=<output dir>)
   Writes patron + silicone preview + mold halves (box_l, box_r) as STL,
   one per file. Naming includes silicone volume in ml for the patron and
   silicone preview.

FLAT WORKFLOW (mb_auto_flat):

1. mb_setup_mm()
2. import_stl(filepath=...)
3. mb_preprocess_patron(...)
4. mb_auto_flat(patron_name="patron", box_gap=4.5, grip_height=10.0)
   One-piece mold, no confirm step needed.
5. mb_export_parts(dir_path=...)

KEY PARAMETERS - what the user usually cares about:

- box_gap (default 4.5): silicone wall thickness in mm. 3-4 for small parts,
  5-6 for bigger ones or low-quality silicone. Less than 3 mm risks tearing.
- box_quality: FAST = preview, MID = default, HIGH = clean output,
  ULTRA = render-quality (slow on big masters).
- key_size (default 4 mm), key_count (default 4): interlock keys to keep
  the two halves aligned. Increase count for tall molds (10cm+).
- join_patron (default True): "Fixed Master" mode — master and base merge.
  If user wants to keep the master separate, set False.
- n_splits=0: keep the box as a single piece (no Y split, no keys).

PITFALLS / KNOWN LIMITS (moldboxer_lite reconstruction):

- adjust_to_contour=True is implemented as uniform spacing, NOT true raycast
  contour. Result may differ from the commercial Moldboxer output on
  highly irregular masters.
- Interlock keys are cubic, not truncated pyramids. They work but are less
  elegant than the original.
- clear_extraction (undercut relief) is NOT implemented. If the master has
  deep undercuts, the mold may bind during demolding.
- Pro features (inner cavity, 2-part silicone) are NOT implemented.

After generating the mold, use the standard print-prep tools
(analyze_mesh_for_print, check_pre_export) on each STL part before sending
it to the slicer.
"""


@mcp.prompt()
def print_prep_strategy() -> str:
    """Defines the preferred strategy for preparing AI-generated STL meshes for FDM 3D printing."""
    return """Your job: take an STL produced by an AI mesh generator (e.g. Meshy)
and turn it into a print-ready file for FDM 3D printing. You are NOT building
models from scratch and you are NOT doing rendering, materials, or animation.

Workflow:

0. Inspect the current scene with get_scene_info(). If a mesh is already loaded,
   skip step 1.

1. Import the source STL with import_stl(filepath=...). Note the reported
   dimensions in mm. AI-generated meshes are often arbitrarily scaled - if the
   bounding box looks wrong for the intended physical size, scale it (and then
   re-run analyze_mesh_for_print to confirm dimensions).

2. Run analyze_mesh_for_print(object_name=...) BEFORE touching anything. This
   gives you the baseline: vertex count, manifold status, hole count, inverted
   normals, disconnected shells.

3. Consult the knowledge base via the blender-kb MCP server for the right
   cleanup recipe. Useful entry points:
   - kb_get_topic("mesh_repair") for non-manifold / holes / inverted normals
   - kb_get_topic("fdm_printing_constraints") for wall thickness, overhangs,
     minimum feature size
   - kb_search("decimate") or kb_search("remesh") if poly count is too high
   - kb_get_topic("print_orientation") for build-plate orientation

   Don't guess - if a topic exists, read it before writing bpy code.

4. Apply the cleanup steps using execute_blender_code. Typical pipeline:
   merge by distance -> fill holes -> recalculate normals outside ->
   (optional) remesh or decimate -> orient flattest face down -> move to origin.

5. Re-run analyze_mesh_for_print. The "ready_to_slice" flag should be True
   and non_manifold_edges should be 0. If not, iterate.

6. PRE-EXPORT obligatory checks (TESTING_LOG rules 25, 30, 36):
   - Call analyze_overhang(object_name) → use the support_decision in Bambu settings.
     Never set "Support: Off" without this check (rule 25).
   - Call render_hires_multiview(object_name, views="TOP,BOTTOM,FRONT") and INSPECT
     the actual PNG files (rule 30: low-res renders hide defects, 5+ false-success
     cases documented in SESSION 004).
   - Call check_pre_export(object_name, expected_contact_points=N) where N is the
     number of expected feet/base points (1 for vases, 4 for animals). Block export
     if ready_to_export is False (rule 36).

7. For sculpt assets with internal membranes (e.g. coral trees, decorative meshes
   with "backing" between branches), see docs/membrane_removal.md. Pipeline:
   - First verify the asset name doesn't contain relief|wall_art|2.5D|plaque
     (= intentional backing, do NOT remove) — rule 41.
   - Try compute_face_visibility_bvh(object_name) to identify interior faces.
   - Or use compute_ao_per_vertex_pymeshlab(input_stl, output_stl) for AO-based
     removal (faster, more robust on coral-tree-like geometry).
   - Stop after 2 failed attempts (rule 31): propose Meshmixer manual workflow.

8. Export with export_stl(object_name=..., filepath=..., apply_modifiers=True).
   File name should end with `_stl.stl` (rule 23).

Hard rules:
- Never add materials, textures, lighting, or animation. Irrelevant for FDM.
- Never download external assets. The user supplies the STL.
- Prefer the structured analyze_mesh_for_print output over parsing free-text
  from execute_blender_code.
- Operations that can mutate the file (export_stl with an existing path) should
  be confirmed with the user if the target already exists and you're not sure.
"""


def main():
    """Run the MCP server"""
    mcp.run()

if __name__ == "__main__":
    main()
