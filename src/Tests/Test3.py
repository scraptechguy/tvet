#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import vispy
import Load

from vispy import app, scene
from vispy.io import read_mesh, load_data_file
from vispy.scene.visuals import Mesh
from vispy.scene import transforms
from vispy.visuals.filters import ShadingFilter, WireframeFilter

from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    global view

    Tk().withdraw()
    filename = askopenfilename()

    def check_filetype():
        for index, character in enumerate(filename):
            if character == ".":
                if filename[index+1:] == "obj":
                    return True
                else:
                    return False

    right_filetype = check_filetype()

    if filename == '':
        print("NO FILE WAS SELECTED")
        vispy.app.quit()
    elif right_filetype == False:
        print("NEEDS TO BE AN .OBJ FILE")
        vispy.app.quit()
    else:
        parser = argparse.ArgumentParser()
        default_mesh = filename
        parser.add_argument('--mesh', default=default_mesh)
        parser.add_argument('--shininess', default=100)
        parser.add_argument('--wireframe-width', default=1)
        args, _ = parser.parse_known_args()

        vertices, faces = Load.load_obj(default_mesh)
        #vertices, faces, normals, texcoords

        canvas = scene.SceneCanvas(keys='interactive', bgcolor='black')
        canvas.size = 1920, 1080
        view = canvas.central_widget.add_view()

        mesh = Mesh(vertices, faces, color='gray')
        mesh.transform = transforms.MatrixTransform()
        mesh.transform.rotate(90, (1, 0, 0))
        mesh.transform.rotate(-45, (0, 0, 1))
        view.add(mesh)

        vispy.scene.visuals.Text("'e' to hide edges", anchor_x='left', pos=(20, 20), font_size=10,
                            color='white', parent=canvas.scene)
        vispy.scene.visuals.Text("'f' to hide faces", anchor_x='left', pos=(20, 40), font_size=10,
                            color='white', parent=canvas.scene)
        vispy.scene.visuals.Text("'s' to change scattering", anchor_x='left', pos=(20, 60), font_size=10,
                            color='white', parent=canvas.scene)
        vispy.scene.visuals.Text("'q' to quit", anchor_x='left', pos=(20, 80), font_size=10,
                            color='white', parent=canvas.scene)
        
        vispy.scene.visuals.Text("Number of vertices: %d" %(len(vertices)), anchor_x='left', pos=(20, 120), font_size=10,
                            color='white', parent=canvas.scene)
        vispy.scene.visuals.Text("Number of faces: %d" %(len(faces)), anchor_x='left', pos=(20, 140), font_size=10,
                            color='white', parent=canvas.scene)

        wireframe_filter = WireframeFilter(width=args.wireframe_width)
        shading_filter = ShadingFilter(shininess=args.shininess)
        mesh.attach(wireframe_filter)
        mesh.attach(shading_filter)

        view.camera = 'turntable'
        view.camera.depth_value = 1e3

        def attach_headlight(view):
            light_dir = (0, 1, 0, 0)
            shading_filter.light_dir = light_dir[:3]
            initial_light_dir = view.camera.transform.imap(light_dir)

            @view.scene.transform.changed.connect
            def on_transform_change(event):
                transform = view.camera.transform
                shading_filter.light_dir = transform.map(initial_light_dir)[:3]

        attach_headlight(view)

        shading_states = (
            dict(shading=None),
            dict(shading='flat'),
            dict(shading='smooth'),
        )

        global shading_state_index
        shading_state_index = shading_states.index(
            dict(shading=shading_filter.shading))

        wireframe_states = (
            dict(wireframe_only=False, faces_only=False,),
            dict(wireframe_only=True, faces_only=False,),
            dict(wireframe_only=False, faces_only=True,),
        )
        
        global wireframe_state_index
        wireframe_state_index = wireframe_states.index(dict(
            wireframe_only=wireframe_filter.wireframe_only,
            faces_only=wireframe_filter.faces_only,
        ))

        def cycle_state(states, index):
            new_index = (index + 1) % len(states)
            return states[new_index], new_index

        @canvas.events.key_press.connect
        def on_key_press(event):
            global shading_state_index
            global wireframe_state_index

            if event.key == 's':
                state, shading_state_index = cycle_state(shading_states,
                                                        shading_state_index)
                for attr, value in state.items():
                    setattr(shading_filter, attr, value)
                mesh.update()
            elif event.key in ['q', 'Q']:
                    vispy.app.quit()
            elif event.key == 'e':
                wireframe_filter.enabled = not wireframe_filter.enabled
                mesh.update()
            elif event.key == 'f':
                state, wireframe_state_index = cycle_state(wireframe_states,
                                                        wireframe_state_index)
                for attr, value in state.items():
                    setattr(wireframe_filter, attr, value)
                mesh.update()

        canvas.show()
        app.run()

if __name__ == "__main__":
    main()