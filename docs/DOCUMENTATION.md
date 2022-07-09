# Documentation

+ Here you can learn about how different segments of <a href="https://github.com/scraptechguy/twet">twet</a> work! 

### Table of contents

+ <a href="https://github.com/scraptechguy/twet/blob/main/docs/DOCUMENTATION.md#loading-ele-node-and-obj">Loading .ele, .node and .obj</a>
+ <a href="https://github.com/scraptechguy/twet/blob/main/docs/DOCUMENTATION.md#saving-ele-node-and-obj">Saving .ele, .node and .obj</a>
+ <a href="https://github.com/scraptechguy/twet/blob/main/docs/DOCUMENTATION.md#line-segment-intersection-in-2d">Line segment intersection in 2D</a>


## Loading .ele, .node and .obj

+ bla bla 

```
```


## Saving .ele, .node and .obj

+ bla bla 

```
```


## Line segment intersection in 2D

Line segment intersection is one of the most basic concepts one needs to understand to get to the bottom of twet. As seen on the image below, two line segments are minding their own business on a plane. Our goal is to determine whether those two intersect.

<div align="center">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/75474651/178101946-bd99bafb-f2fb-4b4f-bf65-a41fe574ae0f.png">
</div>

Each line segment has a beginning and an end. Each of those beginnings and ends have their x and y coordinates. 

### Code structure with snippets of code

+ Yep, we'll be needing that first

```py
import matplotlib.pyplot as plt
```

+ Let's start by defining a function that does the math mentioned above

```py
def intersect_AB_CD(a, b, c, d): 
    nomin = c[1] - a[1] - (c[0] - a[0]) / (a[0] - b[0]) * (a[1] - b[1])
    denom = (c[0] - d[0]) / (a[0] - b[0]) * (a[1] - b[1]) - (c[1] - d[1])
    q = nomin / denom

    e = []

    for i in [0, 1]:
        e.append([c[i] + (c[i] - d[i]) * q])

    return e
```

+ Now it's about time to define `main()` and get some input

```py
def main():
    a = [1, 3]
    b = [4, 4]
    c = [3, 5]
    d = [3.5, 2]
```

+ It would be nice to print out coordinates of the intersection, just to be sure

```py
    intersection = intersect_AB_CD(a, b, c, d)
    print("intersection =" + str(intersection))
```

It's simple as that! Try running the whole thing over here: <a href="https://github.com/scraptechguy/twet/blob/main/docs/segments/line_segment_intersection_2D.py">line_segment_intersection_2D.py</a>
