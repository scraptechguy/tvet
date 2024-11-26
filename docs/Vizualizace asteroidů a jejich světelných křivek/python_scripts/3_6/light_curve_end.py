        total = np.array(total)
        np.savetxt("light_curve.txt", total)

        total[:, 0] = (total[:, 0] - np.min(total[:, 0])) / (np.max(total[:, 0]) - np.min(total[:, 0]))
        total[:, 1] = -(total[:, 1] - np.min(total[:, 1])) / (np.max(total[:, 1]) - np.min(total[:, 1]))

        light_curve = vispy.scene.visuals.Line(pos=(total*200) + (40, 560), color='white', parent=self.canvas.scene)