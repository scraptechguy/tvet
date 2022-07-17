#!/usr/bin/env python3

import matplotlib.pyplot as plt

def intersect_AB_CD(a, b, c, d): 
    # intersection of two line segments in 2D

    nomin = c[1] - a[1] - (c[0] - a[0]) / (a[0] - b[0]) * (a[1] - b[1])
    denom = (c[0] - d[0]) / (a[0] - b[0]) * (a[1] - b[1]) - (c[1] - d[1])
    q = nomin / denom

    e = []

    for i in [0, 1]:
        e.append([c[i] + (c[i] - d[i]) * q])

    return e


def main():
    a = [1, 3]
    b = [4, 4]
    c = [3, 5]
    d = [3.5, 2]

    intersection = intersect_AB_CD(a, b, c, d)
    print("intersection =" + str(intersection))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    lim = max(a + b + c + d) * 1.2 # this incerases plot size by 20 percent so that all points are visible nicely
    ax.set_aspect("equal")
    ax.set_xlim(0, lim)
    ax.set_ylim(0, lim)

    plt.plot([a[0], b[0]], [a[1], b[1]], '+-')
    plt.plot([c[0], d[0]], [c[1], d[1]], '+-')
    plt.plot([intersection[0]], [intersection[1]], '+-')

    plt.show()


if __name__ == "__main__":
    main()

