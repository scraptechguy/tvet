#!/usr/bin/env python3

import Loading
import matplotlib.pyplot as plt

def draw_obj(node, face):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_aspect("equal") # TODO: add size increase

    for i in range(len(face)):
        l, m, n = map(lambda x: x - 1, face[i])

        plt.plot([node[l][0], node[m][0], node[n][0], node[l][0]], [node[l][1], node[m][1], node[n][1], node[l][1]], '-')

    plt.show()

def main(): 
    node, face = Loading.load_obj("/Users/rostislavbroz/Downloads/Taky_nevim/tri_file_octdecv_1.obj")

    draw_obj(node, face)

if __name__ == "__main__": 
    main()
