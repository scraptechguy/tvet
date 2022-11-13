#!/usr/bin/env python3

import Loading
import matplotlib.pyplot as plt

def draw_obj(node, face):
    '''Display a Wavefront OBJ file.''' 
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_aspect("equal") # TODO: add size increase

    for l in range(len(face)):
        i, j, k = face[l]

        plt.plot([node[i][0], node[j][0], node[k][0], node[i][0]], [node[i][1], node[j][1], node[k][1], node[i][1]], '-')

    plt.show()


def main(): 
    node, face = Loading.load_obj("/Users/rostislavbroz/Downloads/Taky_nevim/tri_file_octdecv_1.obj")

    draw_obj(node, face)

if __name__ == "__main__": 
    main()
