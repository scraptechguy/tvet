def main():
    global view

    canvas = vispy.scene.SceneCanvas(keys='interactive')
    canvas.size = 1920, 1080

    view = canvas.central_widget.add_view()