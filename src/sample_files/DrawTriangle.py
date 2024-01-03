#!/usr/bin/env python3

import numpy as np
import vispy.app
import vispy.scene

def main():
    global view

    canvas = vispy.scene.SceneCanvas(keys='interactive')
    canvas.size = 1920, 1080

    view = canvas.central_widget.add_view()

    A = np.array((1, 0, 0))
    B = np.array((0, 1, 0))
    C = np.array((0, 0, 1))

    # Stredy stran
    a = np.array(abs((B - C)))
    b = np.array(abs(C - A))
    c = np.array(abs(A - B))

    # Teziste a normala
    T = 1/3 * (A + B + C)
    n = np.array((np.cross((B - C), (C - A)))/np.dot(abs(B - C), abs(C - A)))

    # Trojúhelník
    vertices = np.array([A, B, C])
    faces = np.array(((0, 1, 2)))
    mesh = vispy.scene.visuals.Mesh(vertices=vertices, faces=faces, vertex_colors=vertices)
    mesh.transform = vispy.scene.transforms.MatrixTransform()
    view.add(mesh)

    # Vrcholy
    markers = vispy.scene.visuals.Markers(pos=vertices, face_color='gray')
    view.add(markers)

    # Normála a popisek
    normal = vispy.scene.visuals.Line(pos=np.array([T, n]), color='white')
    normal_text = vispy.scene.visuals.Text(text="n", pos=T + (0.3, 0.3, 0.45), color='white', font_size=40)
    view.add(normal)
    view.add(normal_text)

    # Těžnice
    median1 = vispy.scene.visuals.Line(pos=np.array([A, a/2]), color='white')
    median2 = vispy.scene.visuals.Line(pos=np.array([B, b/2]), color='white')
    median3 = vispy.scene.visuals.Line(pos=np.array([C, c/2]), color='white')
    view.add(median1)
    view.add(median2)
    view.add(median3)

    # Názvy vrcholů
    for tmp, node in zip(("A","B","C"), vertices):
        text = vispy.scene.visuals.Text(text=tmp, pos=node + 0.03, color='white', font_size=40)
        view.add(text)

    vispy.scene.visuals.Text("'q' to quit", anchor_x='left', anchor_y='bottom', pos=(20, 20), font_size=10,
                        color='white', parent=canvas.scene)

    view.camera = vispy.scene.cameras.turntable.TurntableCamera(fov=30, elevation=0.0, azimuth=0.0)

    axis = vispy.scene.visuals.XYZAxis(parent=view.scene)

    canvas.show()

    @canvas.events.key_press.connect
    def on_key_press(event):
        global view

        if event.key in ['q', 'Q']:
            vispy.app.quit()

        elif event.key in ['Left']:
            view.camera.transform.rotate(-15, (0,0,1))

        elif event.key in ['Right']:
            view.camera.transform.rotate(15, (0,0,1))

        canvas.update()

    vispy.app.run()

if __name__ == "__main__":
    main()