# -*- coding: utf-8 -*-

import os
import numpy as np
import vispy.scene
from vispy.scene import visuals

#
# Make a canvas and add simple view
#
canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()


# generate data

cwd = os.getcwd()

data = np.loadtxt(cwd + "/src/sample_files/sample_data.txt")
pos = data[:, 0:3]
col = data[:, 3:7]
siz = data[:, 7:8].flatten()
# 'disc', 'arrow', 'ring', 'clobber', 'square', 'x', 'diamond', 'vbar', 'hbar', 'cross', 'tailed_arrow', 'triangle_up', 'triangle_down', 'star', 'cross_lines', 'o', '+', '++', 's', '-', '|', '->', '>', '^', 'v', '*'
symbols = np.random.choice(['o', '*', '^', 'diamond'], len(pos))

# create scatter object and fill in the data
scatter = visuals.Markers()
scatter.set_data(pos, edge_width=0, face_color=col, size=siz, symbol=symbols)

view.add(scatter)

view.camera = 'turntable'  # or try 'arcball'

# add a colored 3D axis for orientation
axis = visuals.XYZAxis(parent=view.scene)

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1:
        vispy.app.run()