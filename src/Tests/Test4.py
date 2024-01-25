#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import numpy as np
import vispy.app
import vispy.scene
import tkinter
import tkinter.filedialog

def load_obj(filename, debug=False):
    '''Load a Wavefront OBJ file.''' 
    
    node = []
    face = []

    f = open(filename, "r")

    for line in f.readlines(): 
        if len(line) == 0:
            continue
        elif line[0] == '#': 
            continue

        l = line.split()
        
        if l[0] == 'v':
            node.append(list(map(float, l[1:])))
        elif l[0] == 'f':
            face.append(list(map(lambda x: int(x) - 1, l[1:])))

    f.close()

    if debug:
        print("number of nodes = " + str(len(node)) + ", beginning with node " + str(node[0]))
        print("number of faces = " + str(len(face)) + ", beginning with face " + str(face[0]))

    return np.array(node), np.array(face)

class Asteroid(object):
    canvas = vispy.scene.SceneCanvas(keys='interactive')
    canvas.size = 1920, 1080

    view = canvas.central_widget.add_view()

    def __init__(self, filename=None, args=None):
        self.filename = filename
        self.args = args
        self.vertices, self.faces = None, None
        self.vertices, self.faces = load_obj(self.filename)

        mesh = vispy.scene.visuals.Mesh(vertices=self.vertices, faces=self.faces, color='gray')
        mesh.transform = vispy.scene.transforms.MatrixTransform()
        self.view.add(mesh)

        vispy.scene.visuals.Text("'e' to hide edges", anchor_x='left', pos=(20, 20), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("'f' to hide faces", anchor_x='left', pos=(20, 40), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("'s' to change scattering", anchor_x='left', pos=(20, 60), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("'q' to quit", anchor_x='left', pos=(20, 80), font_size=10,
                            color='white', parent=self.canvas.scene)
        
        vispy.scene.visuals.Text("Number of vertices: %d" %(len(self.vertices)), anchor_x='left', pos=(20, 120), font_size=10,
                            color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("Number of faces: %d" %(len(self.faces)), anchor_x='left', pos=(20, 140), font_size=10,
                            color='white', parent=self.canvas.scene)

        wireframe_filter = vispy.visuals.filters.WireframeFilter(width=self.args.wireframe_width)
        shading_filter = vispy.visuals.filters.ShadingFilter(shininess=self.args.shininess)
        mesh.attach(wireframe_filter)
        mesh.attach(shading_filter)

        self.view.camera = 'turntable'
        self.view.camera.depth_value = 1e3

        def attach_headlight(view):
            light_dir = (0, 1, 0, 0)
            shading_filter.light_dir = light_dir[:3]
            initial_light_dir = self.view.camera.transform.imap(light_dir)

            @view.scene.transform.changed.connect
            def on_transform_change(event):
                transform = self.view.camera.transform
                shading_filter.light_dir = transform.map(initial_light_dir)[:3]

        attach_headlight(self.view)

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

        @self.canvas.events.key_press.connect
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

        self.canvas.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shininess', default=100)
    parser.add_argument('--wireframe-width', default=1)
    args, _ = parser.parse_known_args()

    root = tkinter.Tk()
    root.withdraw()
    filename = tkinter.filedialog.askopenfilename()
    #filename = "src/sample_files/tri_file_octdecv_1.obj"
    asteroid = Asteroid(filename=filename, args=args)

    vispy.app.run()
  
if __name__ == "__main__":
  main()