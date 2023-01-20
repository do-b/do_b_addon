bl_info = {
    "name": "Symmetry",
    "author": "do_b",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "PRESS ALT+W",
    "description": "pie menu for mirror in edit mode",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
from bpy.types import Menu

class SymmetrizeMeshMenu(Menu):
    bl_label = "Symmetrize Mesh"
    bl_idname = "view3D.symmetrize_mesh_menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        operator_enum = context.active_operator.bl_idname.split(".")[-1]
        pie.operator("mesh.symmetrize", text="-X").direction = 'POSITIVE_X'
        pie.operator("mesh.symmetrize", text="+X").direction = 'NEGATIVE_X'
        pie.operator("mesh.symmetrize", text="-Z").direction = 'POSITIVE_Z'
        pie.operator("mesh.symmetrize", text="+Z").direction = 'NEGATIVE_Z'
        pie.operator("mesh.symmetrize", text="").direction = 'POSITIVE_X'
        pie.operator("mesh.symmetrize", text="+Y").direction = 'NEGATIVE_Y'
        pie.operator("mesh.symmetrize", text="-Y").direction = 'POSITIVE_Y'
        pie.operator("mesh.symmetrize", text="").direction = 'NEGATIVE_X'

def register():
    bpy.utils.register_class(SymmetrizeMeshMenu)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Mesh', space_type='EMPTY')
        kmi = km.keymap_items.new("wm.call_menu_pie", "W", "PRESS",alt=True)
        kmi.properties.name = "view3D.symmetrize_mesh_menu"

def unregister():
    bpy.utils.unregister_class(SymmetrizeMeshMenu)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps["Mesh"]
        for kmi in km.keymap_items:
            if kmi.idname == "wm.call_menu_pie":
                if kmi.properties.name == "view3D.symmetrize_mesh_menu":
                    km.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()
