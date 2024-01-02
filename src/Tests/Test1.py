#!/usr/bin/env python3

import numpy as np
import vispy.app
import vispy.scene

def main():

    canvas = vispy.scene.SceneCanvas()
    view = canvas.central_widget.add_view()

    pos = np.array([(1,0,0), (0,1,0), (0,0,1)])
    markers = vispy.scene.visuals.Markers(pos=pos, face_color='red')
    view.add(markers)
    line1 = vispy.scene.visuals.Line(pos=np.array([(0,0,1), (0.5,0.5,0)]), color='red')
    view.add(line1)
    line2 = vispy.scene.visuals.Line(pos=np.array([(0,1,0), (0.5,0,0.5)]), color='red')
    view.add(line2)
    line3 = vispy.scene.visuals.Line(pos=np.array([(1/3,1/3,1/3), (0.66,0.66,0.66)]), color='red')
    view.add(line3)

    vertices = pos
    faces = np.array([(0,1,2)])
    mesh = vispy.scene.visuals.Mesh(vertices=vertices, faces=faces, color='white')
    view.add(mesh)

    view.camera = 'turntable'

    axis = vispy.scene.visuals.XYZAxis(parent=view.scene)

    canvas.show()
    vispy.app.run()

if __name__ == "__main__":
    main()