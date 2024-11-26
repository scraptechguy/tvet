    view.camera = vispy.scene.cameras.turntable.TurntableCamera(fov=30, elevation=0.0, azimuth=0.0)

    axis = vispy.scene.visuals.XYZAxis(parent=view.scene)

    canvas.show()
    vispy.app.run()

if __name__ == "__main__":
    main()