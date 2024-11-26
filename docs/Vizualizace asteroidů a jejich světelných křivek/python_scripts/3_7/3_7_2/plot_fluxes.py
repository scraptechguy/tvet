        def plot_fluxes(phi):
            shading_filter.shading = None
            wireframe_filter.enabled = True
            wireframe_filter.wireframe_only = False
            wireframe_filter.faces_only = False
            normals.visible = False
            color = np.array([0.5, 0.5, 0.5]) / np.percentile(phi, 99)
            face_colors = []
            for face in phi:
                face_colors.append(face * color)
            mesh.set_data(self.vertices, self.faces, face_colors=face_colors)
            mesh.update()