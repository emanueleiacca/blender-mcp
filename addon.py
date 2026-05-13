# Code created by Siddharth Ahuja: www.github.com/ahujasid (c) 2025
# Refocused for STL print-prep workflow.

import bpy
import bmesh
import mathutils
import json
import threading
import socket
import time
import traceback
import io
import os
from bpy.props import IntProperty, BoolProperty
from contextlib import redirect_stdout

bl_info = {
    "name": "Blender MCP (Print Prep)",
    "author": "BlenderMCP",
    "version": (1, 5, 5),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > BlenderMCP",
    "description": "Connect Blender to Claude via MCP for STL print-prep workflow",
    "category": "Interface",
}


class BlenderMCPServer:
    def __init__(self, host='localhost', port=9876):
        self.host = host
        self.port = port
        self.running = False
        self.socket = None
        self.server_thread = None

    def start(self):
        if self.running:
            print("Server is already running")
            return
        self.running = True
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            self.server_thread = threading.Thread(target=self._server_loop)
            self.server_thread.daemon = True
            self.server_thread.start()
            print(f"BlenderMCP server started on {self.host}:{self.port}")
        except Exception as e:
            print(f"Failed to start server: {str(e)}")
            self.stop()

    def stop(self):
        self.running = False
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
            self.socket = None
        if self.server_thread:
            try:
                if self.server_thread.is_alive():
                    self.server_thread.join(timeout=1.0)
            except:
                pass
            self.server_thread = None
        print("BlenderMCP server stopped")

    def _server_loop(self):
        print("Server thread started")
        self.socket.settimeout(1.0)
        while self.running:
            try:
                try:
                    client, address = self.socket.accept()
                    print(f"Connected to client: {address}")
                    client_thread = threading.Thread(target=self._handle_client, args=(client,))
                    client_thread.daemon = True
                    client_thread.start()
                except socket.timeout:
                    continue
                except Exception as e:
                    print(f"Error accepting connection: {str(e)}")
                    time.sleep(0.5)
            except Exception as e:
                print(f"Error in server loop: {str(e)}")
                if not self.running:
                    break
                time.sleep(0.5)
        print("Server thread stopped")

    def _handle_client(self, client):
        print("Client handler started")
        client.settimeout(None)
        buffer = b''
        try:
            while self.running:
                try:
                    data = client.recv(8192)
                    if not data:
                        print("Client disconnected")
                        break
                    buffer += data
                    try:
                        command = json.loads(buffer.decode('utf-8'))
                        buffer = b''

                        def execute_wrapper():
                            try:
                                response = self.execute_command(command)
                                response_json = json.dumps(response)
                                try:
                                    client.sendall(response_json.encode('utf-8'))
                                except:
                                    print("Failed to send response - client disconnected")
                            except Exception as e:
                                print(f"Error executing command: {str(e)}")
                                traceback.print_exc()
                                try:
                                    error_response = {"status": "error", "message": str(e)}
                                    client.sendall(json.dumps(error_response).encode('utf-8'))
                                except:
                                    pass
                            return None

                        bpy.app.timers.register(execute_wrapper, first_interval=0.0)
                    except json.JSONDecodeError:
                        pass
                except Exception as e:
                    print(f"Error receiving data: {str(e)}")
                    break
        except Exception as e:
            print(f"Error in client handler: {str(e)}")
        finally:
            try:
                client.close()
            except:
                pass
            print("Client handler stopped")

    def execute_command(self, command):
        try:
            return self._execute_command_internal(command)
        except Exception as e:
            print(f"Error executing command: {str(e)}")
            traceback.print_exc()
            return {"status": "error", "message": str(e)}

    def _execute_command_internal(self, command):
        cmd_type = command.get("type")
        params = command.get("params", {})

        handlers = {
            "ping": self.ping,
            "get_scene_info": self.get_scene_info,
            "get_object_info": self.get_object_info,
            "get_viewport_screenshot": self.get_viewport_screenshot,
            "execute_code": self.execute_code,
            "get_telemetry_consent": self.get_telemetry_consent,
            "import_stl": self.import_stl,
            "export_stl": self.export_stl,
            "analyze_mesh_for_print": self.analyze_mesh_for_print,
            "analyze_overhang": self.analyze_overhang,
            "check_pre_export": self.check_pre_export,
            "render_hires_multiview": self.render_hires_multiview,
            "compute_face_visibility_bvh": self.compute_face_visibility_bvh,
        }

        handler = handlers.get(cmd_type)
        if handler:
            try:
                print(f"Executing handler for {cmd_type}")
                result = handler(**params)
                print("Handler execution complete")
                return {"status": "success", "result": result}
            except Exception as e:
                print(f"Error in handler: {str(e)}")
                traceback.print_exc()
                return {"status": "error", "message": str(e)}
        else:
            return {"status": "error", "message": f"Unknown command type: {cmd_type}"}

    def ping(self):
        return {"ok": True}

    def get_scene_info(self):
        try:
            print("Getting scene info...")
            scene_info = {
                "name": bpy.context.scene.name,
                "object_count": len(bpy.context.scene.objects),
                "objects": [],
                "unit_system": bpy.context.scene.unit_settings.system,
                "unit_scale_length": bpy.context.scene.unit_settings.scale_length,
            }
            for i, obj in enumerate(bpy.context.scene.objects):
                if i >= 10:
                    break
                scene_info["objects"].append({
                    "name": obj.name,
                    "type": obj.type,
                    "location": [round(float(obj.location.x), 2),
                                 round(float(obj.location.y), 2),
                                 round(float(obj.location.z), 2)],
                })
            print(f"Scene info collected: {len(scene_info['objects'])} objects")
            return scene_info
        except Exception as e:
            print(f"Error in get_scene_info: {str(e)}")
            traceback.print_exc()
            return {"error": str(e)}

    @staticmethod
    def _get_aabb(obj):
        """World-space axis-aligned bounding box (AABB) of a mesh object."""
        if obj.type != 'MESH':
            raise TypeError("Object must be a mesh")
        local_bbox_corners = [mathutils.Vector(corner) for corner in obj.bound_box]
        world_bbox_corners = [obj.matrix_world @ corner for corner in local_bbox_corners]
        min_corner = mathutils.Vector(map(min, zip(*world_bbox_corners)))
        max_corner = mathutils.Vector(map(max, zip(*world_bbox_corners)))
        return [[*min_corner], [*max_corner]]

    @staticmethod
    def _mm_per_unit():
        """How many millimeters one Blender unit represents."""
        return float(bpy.context.scene.unit_settings.scale_length) * 1000.0

    def _dimensions_mm(self, obj):
        bbox = self._get_aabb(obj)
        mm = self._mm_per_unit()
        return [round((bbox[1][i] - bbox[0][i]) * mm, 3) for i in range(3)]

    def get_object_info(self, name):
        obj = bpy.data.objects.get(name)
        if not obj:
            raise ValueError(f"Object not found: {name}")

        obj_info = {
            "name": obj.name,
            "type": obj.type,
            "location": [obj.location.x, obj.location.y, obj.location.z],
            "rotation": [obj.rotation_euler.x, obj.rotation_euler.y, obj.rotation_euler.z],
            "scale": [obj.scale.x, obj.scale.y, obj.scale.z],
            "visible": obj.visible_get(),
            "materials": [slot.material.name for slot in obj.material_slots if slot.material],
        }

        if obj.type == "MESH":
            obj_info["world_bounding_box"] = self._get_aabb(obj)
            obj_info["dimensions_mm"] = self._dimensions_mm(obj)
            mesh = obj.data
            if mesh:
                obj_info["mesh"] = {
                    "vertices": len(mesh.vertices),
                    "edges": len(mesh.edges),
                    "polygons": len(mesh.polygons),
                }
        return obj_info

    def get_viewport_screenshot(self, max_size=800, filepath=None, format="png"):
        try:
            if not filepath:
                return {"error": "No filepath provided"}

            area = next((a for a in bpy.context.screen.areas if a.type == 'VIEW_3D'), None)
            if not area:
                return {"error": "No 3D viewport found"}

            with bpy.context.temp_override(area=area):
                bpy.ops.screen.screenshot_area(filepath=filepath)

            img = bpy.data.images.load(filepath)
            width, height = img.size
            if max(width, height) > max_size:
                scale = max_size / max(width, height)
                new_width = int(width * scale)
                new_height = int(height * scale)
                img.scale(new_width, new_height)
                img.file_format = format.upper()
                img.save()
                width, height = new_width, new_height
            bpy.data.images.remove(img)

            return {"success": True, "width": width, "height": height, "filepath": filepath}
        except Exception as e:
            return {"error": str(e)}

    def execute_code(self, code):
        try:
            namespace = {"bpy": bpy}
            capture_buffer = io.StringIO()
            with redirect_stdout(capture_buffer):
                exec(code, namespace)
            return {"executed": True, "result": capture_buffer.getvalue()}
        except Exception as e:
            raise Exception(f"Code execution error: {str(e)}")

    def get_telemetry_consent(self):
        try:
            addon_prefs = bpy.context.preferences.addons.get(__name__)
            consent = addon_prefs.preferences.telemetry_consent if addon_prefs else True
        except (AttributeError, KeyError):
            consent = True
        return {"consent": consent}

    # ---------- STL print-prep handlers ----------

    @staticmethod
    def _call_stl_import(filepath):
        """Run the right STL import operator across Blender 3.x and 4.x."""
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"STL file not found: {filepath}")
        if hasattr(bpy.ops.wm, "stl_import"):
            bpy.ops.wm.stl_import(filepath=filepath)
        elif hasattr(bpy.ops.import_mesh, "stl"):
            bpy.ops.import_mesh.stl(filepath=filepath)
        else:
            raise RuntimeError("No STL import operator available in this Blender build")

    @staticmethod
    def _call_stl_export(filepath, apply_modifiers):
        """Run the right STL export operator across Blender 3.x and 4.x."""
        if hasattr(bpy.ops.wm, "stl_export"):
            bpy.ops.wm.stl_export(
                filepath=filepath,
                export_selected_objects=True,
                apply_modifiers=apply_modifiers,
            )
        elif hasattr(bpy.ops.export_mesh, "stl"):
            bpy.ops.export_mesh.stl(
                filepath=filepath,
                use_selection=True,
                use_mesh_modifiers=apply_modifiers,
            )
        else:
            raise RuntimeError("No STL export operator available in this Blender build")

    def import_stl(self, filepath, object_name=None):
        existing = set(bpy.data.objects.keys())
        self._call_stl_import(filepath)

        new_objs = [bpy.data.objects[name] for name in bpy.data.objects.keys() if name not in existing]
        if not new_objs:
            raise RuntimeError("STL import produced no new objects")
        obj = new_objs[0]
        if object_name:
            obj.name = object_name

        mesh = obj.data
        return {
            "name": obj.name,
            "source_file": filepath,
            "mesh": {
                "vertices": len(mesh.vertices),
                "edges": len(mesh.edges),
                "polygons": len(mesh.polygons),
            },
            "dimensions_mm": self._dimensions_mm(obj),
            "world_bounding_box": self._get_aabb(obj),
            "unit_scale_length": float(bpy.context.scene.unit_settings.scale_length),
        }

    def export_stl(self, object_name, filepath, apply_modifiers=True):
        obj = bpy.data.objects.get(object_name)
        if not obj:
            raise ValueError(f"Object not found: {object_name}")
        if obj.type != 'MESH':
            raise TypeError(f"Object {object_name} is not a mesh (type={obj.type})")

        out_dir = os.path.dirname(filepath)
        if out_dir and not os.path.isdir(out_dir):
            raise FileNotFoundError(f"Output directory does not exist: {out_dir}")

        # Select only the target object so the exporter picks it up.
        for o in bpy.context.selected_objects:
            o.select_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        self._call_stl_export(filepath, apply_modifiers)

        if not os.path.isfile(filepath):
            raise RuntimeError(f"STL export did not produce a file at {filepath}")

        return {
            "success": True,
            "filepath": filepath,
            "size_bytes": os.path.getsize(filepath),
            "object": obj.name,
            "triangle_count_estimate": len(obj.data.polygons),
            "apply_modifiers": apply_modifiers,
            "dimensions_mm": self._dimensions_mm(obj),
        }

    def analyze_mesh_for_print(self, object_name):
        obj = bpy.data.objects.get(object_name)
        if not obj:
            raise ValueError(f"Object not found: {object_name}")
        if obj.type != 'MESH':
            raise TypeError(f"Object {object_name} is not a mesh (type={obj.type})")

        # Work on an evaluated copy so modifiers are accounted for.
        depsgraph = bpy.context.evaluated_depsgraph_get()
        eval_obj = obj.evaluated_get(depsgraph)
        mesh = eval_obj.to_mesh()

        bm = bmesh.new()
        try:
            bm.from_mesh(mesh)
            bm.normal_update()

            non_manifold_edges = sum(1 for e in bm.edges if not e.is_manifold)
            boundary_edges = [e for e in bm.edges if e.is_boundary]
            boundary_loops = self._count_boundary_loops(boundary_edges)

            degenerate_faces = sum(1 for f in bm.faces if f.calc_area() < 1e-12)

            shells = self._count_shells(bm)

            watertight = non_manifold_edges == 0
            if watertight:
                signed_volume = bm.calc_volume(signed=True)
                mm = self._mm_per_unit()
                signed_volume_mm3 = signed_volume * (mm ** 3)
                normals_consistent = signed_volume_mm3 > 0
                normals_status = "consistent" if normals_consistent else "all_inverted"
            else:
                signed_volume_mm3 = None
                normals_status = "unknown_open_mesh"

            wt_p10, wt_p50, wt_pct_under = self._wall_thickness_stats(
                bm, watertight=watertight,
            )
            inverted_pct = self._inverted_face_pct(bm, watertight=watertight)
            aspect_p95 = self._aspect_ratio_p95(bm)
            dihedral_p90 = self._dihedral_angle_p90(bm)
            bottom_area = self._bottom_contact_area_mm2(bm)
            hull_ratio = self._convex_hull_volume_ratio(bm)
            surface_area = self._surface_area_mm2(bm)
            com_xyz = self._center_of_mass_mm(bm)
            # New metrics (TESTING_LOG rules 25, 27, 29)
            overhang_45_pct = self._overhang_pct(bm, threshold=-0.707)  # cos(45°)
            quasi_flat_ceiling_pct = self._overhang_pct(bm, threshold=-0.97)  # almost-horizontal ceiling
            pca_thickness_ratio = self._pca_thickness_ratio(bm)
            contact_points_count = self._contact_points_count(bm)

            result = {
                "object": obj.name,
                "vertex_count": len(bm.verts),
                "edge_count": len(bm.edges),
                "face_count": len(bm.faces),
                "dimensions_mm": self._dimensions_mm(obj),
                "non_manifold_edges": non_manifold_edges,
                "boundary_edges": len(boundary_edges),
                "boundary_loops": boundary_loops,
                "disconnected_shells": shells,
                "degenerate_faces": degenerate_faces,
                "watertight": watertight,
                "normals": normals_status,
                "signed_volume_mm3": signed_volume_mm3,
                "wall_thickness_p10_mm": wt_p10,
                "wall_thickness_p50_mm": wt_p50,
                "wall_thickness_under_min_pct": wt_pct_under,
                "inverted_face_pct": inverted_pct,
                "aspect_ratio_p95": aspect_p95,
                "dihedral_angle_p90_deg": dihedral_p90,
                "bottom_contact_area_mm2": bottom_area,
                "convex_hull_volume_ratio": hull_ratio,
                "surface_area_mm2": surface_area,
                "center_of_mass_mm": com_xyz,
                # New (rules 25, 27, 29)
                "overhang_45_pct": overhang_45_pct,
                "quasi_flat_ceiling_pct": quasi_flat_ceiling_pct,
                "pca_thickness_ratio": pca_thickness_ratio,
                "contact_points_count": contact_points_count,
            }
            result["ready_to_slice"] = (
                watertight
                and degenerate_faces == 0
                and shells == 1
                and normals_status == "consistent"
            )
            return result
        finally:
            bm.free()
            eval_obj.to_mesh_clear()

    def analyze_overhang(self, object_name):
        """R25 TESTING_LOG: ritorna metriche overhang + decision tree raccomandata
        per supporti. NON tocca la mesh.

        Returns:
            {
              "overhang_45_pct": float 0..100,
              "quasi_flat_ceiling_pct": float 0..100,
              "support_decision": "OFF" | "Auto threshold 45°" | "ON Tree Hybrid OBBLIGATORIO",
              "reasoning": str
            }
        """
        obj = bpy.data.objects.get(object_name)
        if not obj:
            raise ValueError(f"Object not found: {object_name}")
        if obj.type != 'MESH':
            raise TypeError(f"Object {object_name} is not a mesh")

        depsgraph = bpy.context.evaluated_depsgraph_get()
        eval_obj = obj.evaluated_get(depsgraph)
        mesh = eval_obj.to_mesh()
        bm = bmesh.new()
        try:
            bm.from_mesh(mesh)
            bm.normal_update()
            pct_45 = self._overhang_pct(bm, threshold=-0.707) or 0.0
            pct_flat = self._overhang_pct(bm, threshold=-0.97) or 0.0
            # Decision tree (regola 25)
            if pct_45 < 3 and pct_flat < 1:
                decision = "OFF"
                reasoning = "Overhang minimo, supporti non necessari"
            elif pct_45 < 10:
                decision = "Auto threshold 45° (Normal)"
                reasoning = f"Overhang moderato ({pct_45}% a 45°), supporti standard"
            else:
                decision = "ON Tree Hybrid OBBLIGATORIO"
                reasoning = f"Overhang significativo ({pct_45}% a 45°, {pct_flat}% quasi-piatto): Tree Hybrid mandatory"
            return {
                "object": obj.name,
                "overhang_45_pct": pct_45,
                "quasi_flat_ceiling_pct": pct_flat,
                "support_decision": decision,
                "reasoning": reasoning,
            }
        finally:
            bm.free()
            eval_obj.to_mesh_clear()

    def check_pre_export(self, object_name, expected_contact_points=1, z_tolerance_mm=0.5):
        """R36 TESTING_LOG: verifica pre-export OBBLIGATORIA.

        Checks:
        - bbox_z_min == 0 (asset allineato al bed)
        - contact_points_count >= expected_contact_points (= N piedi che toccano bed)
        - manifold (non_manifold_edges == 0, boundary == 0)

        Returns:
            {
              "object": str,
              "bbox_z_min_mm": float,
              "aligned_to_bed": bool,
              "contact_points_count": int,
              "expected_contact_points": int,
              "all_points_touching": bool,
              "manifold_ok": bool,
              "ready_to_export": bool,
              "warnings": [str]
            }
        """
        obj = bpy.data.objects.get(object_name)
        if not obj:
            raise ValueError(f"Object not found: {object_name}")
        if obj.type != 'MESH':
            raise TypeError(f"Object {object_name} is not a mesh")

        depsgraph = bpy.context.evaluated_depsgraph_get()
        eval_obj = obj.evaluated_get(depsgraph)
        mesh = eval_obj.to_mesh()
        bm = bmesh.new()
        try:
            bm.from_mesh(mesh)
            bm.normal_update()
            mm = self._mm_per_unit()
            z_min_mm = min(v.co.z for v in bm.verts) * mm
            aligned = abs(z_min_mm) < 0.01  # entro 10 micron
            cp_count = self._contact_points_count(bm, z_tolerance_mm=z_tolerance_mm)
            nm = sum(1 for e in bm.edges if not e.is_manifold)
            boundary = sum(1 for e in bm.edges if len(e.link_faces) == 1)
            manifold_ok = (nm == 0 and boundary == 0)
            warnings = []
            if not aligned:
                warnings.append(f"BBOX_Z_min = {round(z_min_mm, 3)} mm, NON allineato (atteso 0)")
            if cp_count < expected_contact_points:
                warnings.append(f"Solo {cp_count} punti contatto, attesi {expected_contact_points} (R29: alcuni piedi sospesi?)")
            if not manifold_ok:
                warnings.append(f"Mesh non manifold ({nm} nm_edges, {boundary} boundary)")
            return {
                "object": obj.name,
                "bbox_z_min_mm": round(z_min_mm, 4),
                "aligned_to_bed": aligned,
                "contact_points_count": cp_count,
                "expected_contact_points": expected_contact_points,
                "all_points_touching": cp_count >= expected_contact_points,
                "manifold_ok": manifold_ok,
                "non_manifold_edges": nm,
                "boundary_edges": boundary,
                "ready_to_export": aligned and (cp_count >= expected_contact_points) and manifold_ok,
                "warnings": warnings,
            }
        finally:
            bm.free()
            eval_obj.to_mesh_clear()

    def render_hires_multiview(self, object_name, views=None, resolution_x=1920, resolution_y=1440, output_dir=None):
        """R30 TESTING_LOG: render OpenGL HIRES multi-vista per validazione visiva.

        views: lista di stringhe ['TOP','BOTTOM','FRONT','BACK','LEFT','RIGHT'].
        Salva PNG in output_dir (default: tempdir) con nomi _<view>.png.
        Returns dict con path dei file generati.
        """
        if views is None:
            views = ['TOP', 'BOTTOM', 'FRONT']
        valid_views = {'TOP', 'BOTTOM', 'FRONT', 'BACK', 'LEFT', 'RIGHT'}
        for v in views:
            if v not in valid_views:
                raise ValueError(f"Invalid view '{v}'. Valid: {valid_views}")

        obj = bpy.data.objects.get(object_name)
        if not obj:
            raise ValueError(f"Object not found: {object_name}")

        if output_dir is None:
            output_dir = tempfile.gettempdir()
        os.makedirs(output_dir, exist_ok=True)

        # Setup
        scn = bpy.context.scene
        orig_res_x = scn.render.resolution_x
        orig_res_y = scn.render.resolution_y
        orig_filepath = scn.render.filepath
        scn.render.resolution_x = resolution_x
        scn.render.resolution_y = resolution_y

        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        rendered_files = {}
        try:
            for view in views:
                filepath = os.path.join(output_dir, f"_{object_name}_{view.lower()}.png")
                scn.render.filepath = filepath
                for area in bpy.context.screen.areas:
                    if area.type != 'VIEW_3D':
                        continue
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.shading.type = 'SOLID'
                            space.shading.color_type = 'OBJECT'
                            space.shading.show_xray = False
                            space.region_3d.view_perspective = 'ORTHO'
                    with bpy.context.temp_override(area=area, region=area.regions[-1]):
                        bpy.ops.view3d.view_axis(type=view)
                        bpy.ops.view3d.view_all()
                        bpy.ops.render.opengl(view_context=True, write_still=True)
                    break
                rendered_files[view] = filepath
        finally:
            scn.render.resolution_x = orig_res_x
            scn.render.resolution_y = orig_res_y
            scn.render.filepath = orig_filepath

        return {
            "object": obj.name,
            "resolution": [resolution_x, resolution_y],
            "rendered_files": rendered_files,
            "n_views": len(rendered_files),
        }

    def compute_face_visibility_bvh(self, object_name, n_rays=32, vis_threshold=0.10, ray_distance=10.0):
        """R38 TESTING_LOG: BVHTree raycast hemisphere per identificare facce interne
        (= candidate alla rimozione perché non visibili dall'esterno).

        Per ogni faccia, casta n_rays su semisfera Fibonacci lungo la normale.
        Se < vis_threshold (frazione) raggi escono dal mesh → faccia interna.

        NON cancella nulla, ritorna SOLO la lista degli indici da considerare.
        Decision di delete è dell'utente / playbook successivo.

        Returns:
            {
              "object": str,
              "total_faces": int,
              "interior_face_indices": [int],
              "interior_face_count": int,
              "interior_face_pct": float,
              "params": {n_rays, vis_threshold, ray_distance}
            }
        """
        import math
        from mathutils.bvhtree import BVHTree
        from mathutils import Vector

        obj = bpy.data.objects.get(object_name)
        if not obj:
            raise ValueError(f"Object not found: {object_name}")
        if obj.type != 'MESH':
            raise TypeError(f"Object {object_name} is not a mesh")

        depsgraph = bpy.context.evaluated_depsgraph_get()
        eval_obj = obj.evaluated_get(depsgraph)
        mesh = eval_obj.to_mesh()
        bm = bmesh.new()
        interior = []
        try:
            bm.from_mesh(mesh)
            bm.normal_update()
            bm.faces.ensure_lookup_table()
            bvh = BVHTree.FromBMesh(bm)
            EPS = 1e-4

            # Fibonacci hemisphere points (locale, asse Z up)
            base_pts = []
            for i in range(n_rays):
                phi = math.acos(1 - (i + 0.5) / n_rays)
                theta = math.pi * (1 + 5 ** 0.5) * i
                base_pts.append(Vector((
                    math.sin(phi) * math.cos(theta),
                    math.sin(phi) * math.sin(theta),
                    math.cos(phi),
                )))

            total = len(bm.faces)
            for f in bm.faces:
                if f.normal.length_squared <= 0:
                    continue
                origin = f.calc_center_median() + f.normal * EPS
                rot = Vector((0, 0, 1)).rotation_difference(f.normal).to_matrix()
                free = 0
                for d_local in base_pts:
                    d = rot @ d_local
                    hit, *_ = bvh.ray_cast(origin, d, ray_distance)
                    if hit is None:
                        free += 1
                if free / n_rays < vis_threshold:
                    interior.append(f.index)

            return {
                "object": obj.name,
                "total_faces": total,
                "interior_face_indices": interior,
                "interior_face_count": len(interior),
                "interior_face_pct": round(100.0 * len(interior) / total, 1) if total > 0 else 0.0,
                "params": {
                    "n_rays": n_rays,
                    "vis_threshold": vis_threshold,
                    "ray_distance": ray_distance,
                },
            }
        finally:
            bm.free()
            eval_obj.to_mesh_clear()

    def _wall_thickness_stats(self, bm, watertight, max_samples=5000):
        """Raycast-based wall thickness distribution.

        Returns (p10_mm, p50_mm, pct_under_0_8_mm) or (None, None, None) when
        the metric is unreliable (open mesh, no faces, all rays miss).

        Why these three: p10 catches the thinnest 10% of the surface (most
        likely to be silently skipped by the slicer); p50 is the median, useful
        as a sanity baseline; pct_under_0_8 is the share of surface below the
        FDM 0.4mm-nozzle 2-perimeter floor.

        Samples up to `max_samples` face centroids to keep timing bounded;
        face count over 5k uses deterministic random sampling (seed=42).
        """
        if not watertight or len(bm.faces) == 0:
            return None, None, None

        from mathutils.bvhtree import BVHTree

        bvh = BVHTree.FromBMesh(bm)
        mm = self._mm_per_unit()

        faces = list(bm.faces)
        if len(faces) > max_samples:
            import random
            rng = random.Random(42)
            faces = rng.sample(faces, max_samples)

        distances_mm = []
        epsilon = 1e-6
        for face in faces:
            if face.normal.length_squared <= 0:
                continue
            # Step inward by epsilon so the raycast doesn't hit the origin face itself.
            origin = face.calc_center_median() + face.normal * (-epsilon)
            direction = -face.normal
            hit_loc, _, _, dist = bvh.ray_cast(origin, direction)
            if hit_loc is None or dist is None:
                continue
            distances_mm.append(dist * mm)

        if not distances_mm:
            return None, None, None

        distances_mm.sort()
        n = len(distances_mm)
        p10 = distances_mm[int(n * 0.10)]
        p50 = distances_mm[int(n * 0.50)]
        pct_under = sum(1 for d in distances_mm if d < 0.8) / n
        return round(p10, 3), round(p50, 3), round(pct_under * 100, 1)

    def _inverted_face_pct(self, bm, watertight, max_samples=5000):
        """Percentage of faces whose normal points INTO the mesh body.

        Approach: for a watertight mesh, the outward direction of any face is
        unobstructed (the ray escapes to infinity). If a face's normal points
        INWARD, a ray cast along it crosses the opposite wall of the mesh and
        registers a hit. The ratio hits / sampled is the share of inverted
        faces.

        Returns a float in [0, 100], or None if the mesh isn't watertight
        (the metric is meaningless on open meshes).
        """
        if not watertight or len(bm.faces) == 0:
            return None

        from mathutils.bvhtree import BVHTree

        bvh = BVHTree.FromBMesh(bm)

        faces = list(bm.faces)
        if len(faces) > max_samples:
            import random
            rng = random.Random(43)  # different seed from wall thickness
            faces = rng.sample(faces, max_samples)

        epsilon = 1e-6
        inverted = 0
        valid = 0
        for face in faces:
            if face.normal.length_squared <= 0:
                continue
            origin = face.calc_center_median() + face.normal * epsilon
            direction = face.normal
            hit_loc, _, _, _ = bvh.ray_cast(origin, direction)
            valid += 1
            if hit_loc is not None:
                inverted += 1
        if valid == 0:
            return None
        return round(100.0 * inverted / valid, 1)

    def _aspect_ratio_p95(self, bm, max_samples=5000):
        """95th percentile of face edge-length aspect ratio (max/min).

        Why: a value above 10 indicates sliver triangles (degenerate-shape
        but not zero-area) typical of post-decimate damage. An ideal mesh
        sits below 4. Cheap proxy for visual "long thin triangles" check
        that the assistant can never see otherwise.
        """
        if len(bm.faces) == 0:
            return None
        faces = list(bm.faces)
        if len(faces) > max_samples:
            import random
            rng = random.Random(44)
            faces = rng.sample(faces, max_samples)
        ratios = []
        for f in faces:
            lens = [e.calc_length() for e in f.edges]
            mn = min(lens)
            if mn <= 1e-12:
                continue
            ratios.append(max(lens) / mn)
        if not ratios:
            return None
        ratios.sort()
        idx = int(len(ratios) * 0.95)
        return round(ratios[min(idx, len(ratios) - 1)], 2)

    def _dihedral_angle_p90(self, bm, max_samples=5000):
        """90th percentile of dihedral angle across manifold edges, in degrees.

        Why: high value (> ~60deg) flags sharp folds that the slicer renders
        as visible edges. Useful to compare orientation candidates without
        viewport access.
        """
        edges = [e for e in bm.edges if e.is_manifold and len(e.link_faces) == 2]
        if not edges:
            return None
        if len(edges) > max_samples:
            import random
            rng = random.Random(45)
            edges = rng.sample(edges, max_samples)
        import math
        angles_deg = []
        for e in edges:
            try:
                rad = e.calc_face_angle(0.0)
            except (ValueError, RuntimeError):
                continue
            angles_deg.append(math.degrees(rad))
        if not angles_deg:
            return None
        angles_deg.sort()
        idx = int(len(angles_deg) * 0.90)
        return round(angles_deg[min(idx, len(angles_deg) - 1)], 1)

    def _bottom_contact_area_mm2(self, bm, normal_z_threshold=-0.95):
        """Area of faces facing downward (normal.z <= -0.95), in mm^2.

        Why: proxy for build-plate adhesion area. A part with high contact
        area is stable during print without brim; a part with low contact
        area may tip. Independent of bbox — a tripod has small bbox-bottom
        area but the contact area may still be acceptable.
        """
        if len(bm.faces) == 0:
            return None
        mm = self._mm_per_unit()
        area_bu = 0.0
        for f in bm.faces:
            if f.normal.length_squared <= 0:
                continue
            if f.normal.z <= normal_z_threshold:
                area_bu += f.calc_area()
        return round(area_bu * (mm ** 2), 2)

    def _convex_hull_volume_ratio(self, bm):
        """volume(mesh) / volume(convex_hull). Range (0, 1].

        Why: 1.0 = the mesh IS its convex hull (a brick); near 0 = thin spiky
        shape. Catches "spiky / fragile silhouette" patterns from AI mesh
        without needing a screenshot. Returns None if the mesh isn't closed
        (signed volume meaningless).
        """
        try:
            mesh_vol = bm.calc_volume(signed=False)
        except (ValueError, RuntimeError):
            return None
        if mesh_vol <= 0:
            return None
        try:
            import bmesh as _bm
            hull_bm = _bm.new()
            for v in bm.verts:
                hull_bm.verts.new(v.co)
            hull_bm.verts.ensure_lookup_table()
            geom = list(hull_bm.verts)
            _bm.ops.convex_hull(hull_bm, input=geom)
            hull_vol = hull_bm.calc_volume(signed=False)
            hull_bm.free()
        except Exception:
            return None
        if hull_vol <= 0:
            return None
        return round(min(mesh_vol / hull_vol, 1.0), 3)

    def _surface_area_mm2(self, bm):
        """Total surface area in mm^2.

        Why: input for print-time estimate and PLA cost calculation.
        surface_area_mm2 * wall_thickness_mm / 1000 ≈ shell volume in cm^3;
        multiply by 1.24 g/cm^3 for PLA mass (excluding infill).
        """
        if len(bm.faces) == 0:
            return None
        mm = self._mm_per_unit()
        area_bu = sum(f.calc_area() for f in bm.faces)
        return round(area_bu * (mm ** 2), 2)

    def _center_of_mass_mm(self, bm):
        """Area-weighted centroid of the surface, in mm coordinates [x, y, z].

        Why: surface centroid approximates the printed part's center of mass
        (uniform shell + uniform infill). The assistant can compare CoM_xy
        against the bottom-contact bbox to flag tipping risk during print.
        Not the true CoM of the printed solid (that depends on infill
        pattern), but a usable proxy.
        """
        if len(bm.faces) == 0:
            return None
        mm = self._mm_per_unit()
        total_area = 0.0
        cx = cy = cz = 0.0
        for f in bm.faces:
            a = f.calc_area()
            if a <= 0:
                continue
            c = f.calc_center_median()
            cx += c.x * a
            cy += c.y * a
            cz += c.z * a
            total_area += a
        if total_area <= 0:
            return None
        return [
            round((cx / total_area) * mm, 3),
            round((cy / total_area) * mm, 3),
            round((cz / total_area) * mm, 3),
        ]

    def _overhang_pct(self, bm, threshold=-0.707, bed_z_offset=0.5):
        """Percentuale di area facce con normal.z sotto soglia (= overhang/ceiling).

        threshold=-0.707 (cos 45°) → R25 pct_overhang_45.
        threshold=-0.97 (~14° dall'orizzontale) → R25 quasi_flat_ceiling.
        bed_z_offset: escludi facce con centro Z < bed_z_offset (= la backplane voluta
        sul bed) per non contare la base come overhang.

        Returns float 0..100, None se nessuna faccia.
        """
        if len(bm.faces) == 0:
            return None
        total = 0.0
        below = 0.0
        for f in bm.faces:
            if f.normal.length_squared <= 0:
                continue
            a = f.calc_area()
            total += a
            if f.normal.z < threshold:
                center = f.calc_center_median()
                if center.z > bed_z_offset:
                    below += a
        if total <= 0:
            return None
        return round(100.0 * below / total, 1)

    def _pca_thickness_ratio(self, bm):
        """Rapporto autovalore minimo / massimo della covarianza dei vertici (PCA).

        R27 TESTING_LOG: <10% → bassorilievo netto, anche se piano inclinato.
        10-30% → ambiguo. >30% → asset 3D pieno.

        Returns float 0..1, None se < 4 vertici.
        """
        n = len(bm.verts)
        if n < 4:
            return None
        try:
            # Estrai coordinate via foreach_get equivalente puro Python
            coords = [v.co for v in bm.verts]
            # Centroide
            cx = sum(c.x for c in coords) / n
            cy = sum(c.y for c in coords) / n
            cz = sum(c.z for c in coords) / n
            # Covarianza simmetrica 3x3
            sxx = syy = szz = sxy = sxz = syz = 0.0
            for c in coords:
                dx, dy, dz = c.x - cx, c.y - cy, c.z - cz
                sxx += dx * dx
                syy += dy * dy
                szz += dz * dz
                sxy += dx * dy
                sxz += dx * dz
                syz += dy * dz
            sxx /= n; syy /= n; szz /= n
            sxy /= n; sxz /= n; syz /= n
            # Eigenvalues di matrice simmetrica 3x3 via formula chiusa (Smith 1961).
            # Tracce di potenza usate per evitare dipendenza numpy nell'addon Blender.
            from mathutils import Matrix
            M = Matrix(((sxx, sxy, sxz), (sxy, syy, syz), (sxz, syz, szz)))
            # mathutils non espone eigenvalues. Calcolo via determinante + traccia
            # NB: per uso solo come ratio, usiamo proxy via SVD-equivalente:
            # M = R @ D @ R^T → autovalori sono i valori sulla diagonale D
            # Approccio robusto: power iteration su matrice 3x3.
            # SOLUZIONE SEMPLICE: usa diagonalizzazione tramite iterazioni Jacobi.
            evals = self._jacobi_eigenvalues_3x3(M)
            evals.sort()  # ascending
            if evals[2] <= 1e-12:
                return None
            return round(evals[0] / evals[2], 4)
        except Exception:
            return None

    @staticmethod
    def _jacobi_eigenvalues_3x3(M, max_iter=20, tol=1e-9):
        """Jacobi rotation per matrice simmetrica 3x3. Restituisce 3 autovalori."""
        import math
        # Estrae elementi
        a = [[M[0][0], M[0][1], M[0][2]],
             [M[1][0], M[1][1], M[1][2]],
             [M[2][0], M[2][1], M[2][2]]]
        for _ in range(max_iter):
            # Trova off-diagonal max
            p, q = 0, 1
            mx = abs(a[0][1])
            if abs(a[0][2]) > mx:
                p, q, mx = 0, 2, abs(a[0][2])
            if abs(a[1][2]) > mx:
                p, q, mx = 1, 2, abs(a[1][2])
            if mx < tol:
                break
            # Rotazione
            theta = (a[q][q] - a[p][p]) / (2.0 * a[p][q]) if a[p][q] != 0 else 0
            t = math.copysign(1.0 / (abs(theta) + math.sqrt(theta * theta + 1)), theta) if theta != 0 else 1.0
            c = 1.0 / math.sqrt(1 + t * t)
            s = t * c
            # Applica rotazione
            app = a[p][p]
            aqq = a[q][q]
            apq = a[p][q]
            a[p][p] = c * c * app - 2 * s * c * apq + s * s * aqq
            a[q][q] = s * s * app + 2 * s * c * apq + c * c * aqq
            a[p][q] = 0.0
            a[q][p] = 0.0
            for r in range(3):
                if r != p and r != q:
                    arp = a[r][p]
                    arq = a[r][q]
                    a[r][p] = c * arp - s * arq
                    a[p][r] = a[r][p]
                    a[r][q] = s * arp + c * arq
                    a[q][r] = a[r][q]
        return [a[0][0], a[1][1], a[2][2]]

    def _contact_points_count(self, bm, z_tolerance_mm=0.5, cluster_radius_mm=8.0):
        """Numero di "piedi" che toccano il bed (cluster XY di vertici a Z basso).

        R29 TESTING_LOG: per animali/figurine multi-piede, verifica che N punti
        di appoggio raggiungano effettivamente il bed (Z < tolerance).

        Returns int >= 0.
        """
        mm = self._mm_per_unit()
        z_tol_bu = z_tolerance_mm / mm
        r_bu = cluster_radius_mm / mm
        r2 = r_bu * r_bu
        # Vertici a Z basso
        low_verts = [v.co for v in bm.verts if v.co.z < z_tol_bu]
        if not low_verts:
            return 0
        # DBSCAN-like cluster XY
        n = len(low_verts)
        assigned = [-1] * n
        clusters = 0
        for i in range(n):
            if assigned[i] != -1:
                continue
            stack = [i]
            while stack:
                j = stack.pop()
                if assigned[j] != -1:
                    continue
                assigned[j] = clusters
                for k in range(n):
                    if assigned[k] != -1:
                        continue
                    dx = low_verts[j].x - low_verts[k].x
                    dy = low_verts[j].y - low_verts[k].y
                    if dx * dx + dy * dy < r2:
                        stack.append(k)
            clusters += 1
        return clusters

    @staticmethod
    def _count_boundary_loops(boundary_edges):
        """Count how many closed loops the boundary edges form."""
        edge_set = set(e.index for e in boundary_edges)
        edge_by_index = {e.index: e for e in boundary_edges}
        visited = set()
        loops = 0
        for start_idx in list(edge_set):
            if start_idx in visited:
                continue
            loops += 1
            stack = [start_idx]
            while stack:
                idx = stack.pop()
                if idx in visited:
                    continue
                visited.add(idx)
                edge = edge_by_index[idx]
                for v in edge.verts:
                    for linked in v.link_edges:
                        if linked.index in edge_set and linked.index not in visited:
                            stack.append(linked.index)
        return loops

    @staticmethod
    def _count_shells(bm):
        """Count disconnected mesh islands (shells) via BFS over shared edges."""
        unvisited = set(f.index for f in bm.faces)
        face_by_index = {f.index: f for f in bm.faces}
        shells = 0
        while unvisited:
            shells += 1
            start = next(iter(unvisited))
            stack = [start]
            while stack:
                fi = stack.pop()
                if fi not in unvisited:
                    continue
                unvisited.remove(fi)
                face = face_by_index[fi]
                for edge in face.edges:
                    for linked in edge.link_faces:
                        if linked.index in unvisited:
                            stack.append(linked.index)
        return shells


# Blender Addon Preferences
class BLENDERMCP_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    telemetry_consent: BoolProperty(
        name="Allow Telemetry",
        description="Allow collection of prompts, code snippets, and screenshots to help improve Blender MCP",
        default=True,
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Telemetry & Privacy:", icon='PREFERENCES')
        box = layout.box()
        row = box.row()
        row.prop(self, "telemetry_consent", text="Allow Telemetry")
        box.separator()
        if self.telemetry_consent:
            box.label(text="With consent: We collect anonymized prompts, code, and screenshots.", icon='INFO')
        else:
            box.label(text="Without consent: We only collect minimal anonymous usage data", icon='INFO')
            box.label(text="(tool names, success/failure, duration - no prompts or code).", icon='BLANK1')
        box.separator()
        box.label(text="All data is fully anonymized. You can change this anytime.", icon='CHECKMARK')
        box.separator()
        row = box.row()
        row.operator("blendermcp.open_terms", text="View Terms and Conditions", icon='TEXT')


class BLENDERMCP_PT_Panel(bpy.types.Panel):
    bl_label = "Blender MCP"
    bl_idname = "BLENDERMCP_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BlenderMCP'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "blendermcp_port")
        layout.label(text="Focus: STL print-prep")
        if not scene.blendermcp_server_running:
            layout.operator("blendermcp.start_server", text="Connect to MCP server")
        else:
            layout.operator("blendermcp.stop_server", text="Disconnect from MCP server")
            layout.label(text=f"Running on port {scene.blendermcp_port}")


class BLENDERMCP_OT_StartServer(bpy.types.Operator):
    bl_idname = "blendermcp.start_server"
    bl_label = "Connect to Claude"
    bl_description = "Start the BlenderMCP server to connect with Claude"

    def execute(self, context):
        scene = context.scene
        if not hasattr(bpy.types, "blendermcp_server") or not bpy.types.blendermcp_server:
            bpy.types.blendermcp_server = BlenderMCPServer(port=scene.blendermcp_port)
        bpy.types.blendermcp_server.start()
        scene.blendermcp_server_running = True
        return {'FINISHED'}


class BLENDERMCP_OT_StopServer(bpy.types.Operator):
    bl_idname = "blendermcp.stop_server"
    bl_label = "Stop the connection to Claude"
    bl_description = "Stop the connection to Claude"

    def execute(self, context):
        scene = context.scene
        if hasattr(bpy.types, "blendermcp_server") and bpy.types.blendermcp_server:
            bpy.types.blendermcp_server.stop()
            del bpy.types.blendermcp_server
        scene.blendermcp_server_running = False
        return {'FINISHED'}


class BLENDERMCP_OT_OpenTerms(bpy.types.Operator):
    bl_idname = "blendermcp.open_terms"
    bl_label = "View Terms and Conditions"
    bl_description = "Open the Terms and Conditions document"

    def execute(self, context):
        terms_url = "https://github.com/ahujasid/blender-mcp/blob/main/TERMS_AND_CONDITIONS.md"
        try:
            import webbrowser
            webbrowser.open(terms_url)
            self.report({'INFO'}, "Terms and Conditions opened in browser")
        except Exception as e:
            self.report({'ERROR'}, f"Could not open Terms and Conditions: {str(e)}")
        return {'FINISHED'}


def register():
    bpy.types.Scene.blendermcp_port = IntProperty(
        name="Port",
        description="Port for the BlenderMCP server",
        default=9876,
        min=1024,
        max=65535,
    )
    bpy.types.Scene.blendermcp_server_running = BoolProperty(name="Server Running", default=False)

    bpy.utils.register_class(BLENDERMCP_AddonPreferences)
    bpy.utils.register_class(BLENDERMCP_PT_Panel)
    bpy.utils.register_class(BLENDERMCP_OT_StartServer)
    bpy.utils.register_class(BLENDERMCP_OT_StopServer)
    bpy.utils.register_class(BLENDERMCP_OT_OpenTerms)
    print("BlenderMCP addon registered")


def unregister():
    if hasattr(bpy.types, "blendermcp_server") and bpy.types.blendermcp_server:
        bpy.types.blendermcp_server.stop()
        del bpy.types.blendermcp_server

    bpy.utils.unregister_class(BLENDERMCP_PT_Panel)
    bpy.utils.unregister_class(BLENDERMCP_OT_StartServer)
    bpy.utils.unregister_class(BLENDERMCP_OT_StopServer)
    bpy.utils.unregister_class(BLENDERMCP_OT_OpenTerms)
    bpy.utils.unregister_class(BLENDERMCP_AddonPreferences)

    del bpy.types.Scene.blendermcp_port
    del bpy.types.Scene.blendermcp_server_running
    print("BlenderMCP addon unregistered")


if __name__ == "__main__":
    register()
