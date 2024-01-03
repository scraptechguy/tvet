#!/usr/bin/env python3

import Load
import matplotlib.pyplot as plt

def draw_obj(node, face):
    '''Display a Wavefront OBJ file.''' 
    
    plt.style.use('dark_background')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax = plt.axes(projection="3d")
    ax.set_aspect("equal") # TODO: add size increase
    ax.set_axis_off()

    for l in range(len(face)):
        i, j, k = face[l]

        plt.plot([node[i][0], node[j][0], node[k][0], node[i][0]], [node[i][1], node[j][1], node[k][1], node[i][1]], [node[i][2], node[j][2], node[k][2], node[i][2]], '-')

    plt.show()


def main(): 
    node, face = Load.load_obj("src/sample_files/tri_file_octdecv_1.obj")

    draw_obj(node, face)

if __name__ == "__main__": 
    main()
