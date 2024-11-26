    # Trojuhelnik
    vertices = np.array([A, B, C])
    faces = np.array(((0, 1, 2)))
    mesh = vispy.scene.visuals.Mesh(vertices=vertices, faces=faces, vertex_colors=vertices)
    mesh.transform = vispy.scene.transforms.MatrixTransform()
    view.add(mesh)

    # Vrcholy
    markers = vispy.scene.visuals.Markers(pos=vertices, face_color='gray')
    view.add(markers)

    # Normala a popisek
    normal = vispy.scene.visuals.Line(pos=np.array([T, n]), color='white')
    text = vispy.scene.visuals.Text(text="n", pos=T + (0.3, 0.3, 0.45), color='white', font_size=40)
    view.add(normal)
    view.add(text)

    # Teznice
    median1 = vispy.scene.visuals.Line(pos=np.array([A, a/2]), color='white')
    median2 = vispy.scene.visuals.Line(pos=np.array([B, b/2]), color='white')
    median3 = vispy.scene.visuals.Line(pos=np.array([C, c/2]), color='white')
    view.add(median1)
    view.add(median2)
    view.add(median3)

    # Nazvy vrcholu
    for tmp, node in zip(("A","B","C"), vertices):
        text = vispy.scene.visuals.Text(text=tmp, pos=node + 0.03, color='white', font_size=40)
        view.add(text)