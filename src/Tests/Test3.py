#!/usr/bin/env python3

import numpy as np
import vispy.app
import vispy.scene

import Load

def main():
    global view

    canvas = vispy.scene.SceneCanvas(keys='interactive')
    canvas.size = 1920, 1080
    view = canvas.central_widget.add_view()

    vertices, faces = Load.load_obj("src/sample_files/tri_file_octdecv_1.obj")
    mesh = vispy.scene.visuals.Mesh(vertices=np.array(vertices), faces=np.array(faces), color='gray')

    view.add(mesh)

    view.camera = 'turntable'
    axis = vispy.scene.visuals.XYZAxis(parent=view.scene)
    view.add(axis)

    canvas.show()
    vispy.app.run()

if __name__ == "__main__":
    main()