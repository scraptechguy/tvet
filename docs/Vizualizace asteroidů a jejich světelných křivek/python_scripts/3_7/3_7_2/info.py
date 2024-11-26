        s = vispy.scene.visuals.Line(pos=np.array([(0, 0.02, 0), self.s + (0, 0.02, 0)]), color='yellow', parent=self.view.scene)
        o = vispy.scene.visuals.Line(pos=np.array([(0, 0.02, 0), self.o + (0, 0.02, 0)]), color='magenta', parent=self.view.scene)
        
        vispy.scene.visuals.Text("'1' to show phi_i", anchor_x='left', pos=(20, 20), font_size=10, color='white', parent=self.canvas.scene)
        vispy.scene.visuals.Text("'2' to show phi_e", anchor_x='left', pos=(20, 40), font_size=10, color='white', parent=self.canvas.scene)
...