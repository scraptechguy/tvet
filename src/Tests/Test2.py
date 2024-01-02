#!/usr/bin/env python3

import numpy as np
import vispy.app
import vispy.scene

def main():
  global view

  canvas = vispy.scene.SceneCanvas(keys='interactive')
  canvas.size = 1920, 1080

  view = canvas.central_widget.add_view()

  A = (1, 0, 0)
  B = (0, 1, 0)
  C = (0, 0, 1)
  nodes = np.array([A, B, C])
  faces = np.array(((0, 1, 2)))
  mesh = vispy.scene.visuals.Mesh(vertices=nodes, faces=faces, vertex_colors=nodes)
  mesh.transform = vispy.scene.transforms.MatrixTransform()
  view.add(mesh)

  markers = vispy.scene.visuals.Markers(pos=nodes, face_color='gray')
  view.add(markers)

  for tmp, node in zip(("A","B","C"), nodes):
    text = vispy.scene.visuals.Text(text=tmp, pos=node+0.02, color='white', font_size=20)
    view.add(text)

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