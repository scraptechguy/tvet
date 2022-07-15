# Key concepts

+ Here you can learn about different concepts <a href="https://github.com/scraptechguy/twet">twet</a> is built on! 

### Table of contents

+ <a href="https://github.com/scraptechguy/twet/blob/main/docs/CONCEPTS.md#loading-ele-node-face-and-obj">Loading .ele, .node, .face and .obj</a>
+ <a href="https://github.com/scraptechguy/twet/blob/main/docs/CONCEPTS.md#saving-ele-node-and-obj">Saving .ele, .node and .obj</a>
+ <a href="https://github.com/scraptechguy/twet/blob/main/docs/CONCEPTS.md#line-segment-intersection-in-2d">Line segment intersection in 2D</a>


## Loading .ele, .node, .face and .obj

Our goal here is to create a library that can be used to load `.ele`, `.node`, `.face` and `.obj` files.

### .ele

An `.ele` file is a text file that contains the element connectivity information. Here's an example:

```py
50809  4  0
    1    8801  8536  9111 10466
    2    8167  9851 10065 10844
    3    6285  7082  7646 10698
    4    4268  3177  4617  7884
```

### .node

An `.node` file is a text file that contains the node information. This is how it looks like:

```py
11218  3  0  0
   1    0  0  57.616300000000003
   2    14.6698  0  59.806100000000001
   3    0  15.9201  58.651499999999999
   4    -14.321099999999999  0  54.226700000000001
```

### .face

An `.face` file is a text file that contains the face information. Here's how one can look like:

```py
12008  1
    1   2707     6  4718    1
    2   1662  2728  5495    1
    3   1612  2705  5527    1
    4   1603   407  5525    1
```

### .obj

An `.obj` file is a file that contains the vertices of a 3D model. It looks something like this:

```py
v 0.0000 0.0000 57.6163
v 14.6698 0.0000 59.8061
v 0.0000 15.9201 58.6515
f 1 2 3
f 1 3 4
f 1 4 5
```

The three numbers after the `v` are the x, y and z coordinates of the vertex. The three numbers after `f` are the indices of the vertices that make up the face.

Our goal here is process the `.obj` file and create a list of vertices and a list of faces.

+ Let's begin by defining a function that takes filepath as an argument and returns a list of nodes and a list of faces. The `print_info` argument prints out a simple info about the lists if set to true (it's like that by default).

```py
def load_obj(filename, print_info=True):
    '''Load a Wavefront OBJ file.''' 
    
    node = []
    face = []
```

+ Now we have to open the file and read the contents. 

```py
    f = open(filename, "r")
```

+ To get all the important information, we got to loop through the file and differentiate between the different types of lines and append the conents to our lists accordingly. 

```py
    for line in f.readlines():
        # Skip blank lines and comments
          
        if len(line) == 0:
            continue
        elif line[0] == '#': 
            continue

        l = line.split()
        
        if l[0] == 'v':
            node.append(list(map(float, l[1:])))
        elif l[0] == 'f':
            face.append(list(map(int, l[1:])))
```

+ Let's close the file as soon as possible and if not said otherwise, print out some info about our lists. 

```py
    f.close()

    if print_info:
        print("number of nodes = " + str(len(node)) + ", beginning with node " + str(node[0]))
        print("number of faces = " + str(len(face)) + ", beginning with face " + str(face[0]))
```

+ Now all that's left is to return the lists. 

```py
    return node, face
```

And we're done! Try running the whole thing over here: <a href="https://github.com/scraptechguy/twet/blob/main/docs/segments/load_obj.py">load_obj.py</a>

<div align="right">
  <a href="https://github.com/scraptechguy/twet/blob/main/docs/CONCEPTS.md#key-concepts">^</a>
</div>


## Saving .ele, .node and .obj

+ bla bla 

```
```

<div align="right">
  <a href="https://github.com/scraptechguy/twet/blob/main/docs/CONCEPTS.md#key-concepts">^</a>
</div>


## Line segment intersection in 2D

<a href="https://en.wikipedia.org/wiki/Line_segment">Line segment</a> intersection is one of the most basic concepts one needs to understand to get to the bottom of twet. As seen on the image below, two line segments are minding their own business on a plane. Our goal is to determine whether those two intersect.

<div align="center">
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/75474651/178101946-bd99bafb-f2fb-4b4f-bf65-a41fe574ae0f.png">
</div>

Each line segment has a beginning and an end. Each of those beginnings and ends have their own x and y coordinates. Those shell be our input. 

```
a = [1, 3]
b = [4, 4]
c = [3, 5]
d = [3.5, 2]
```


### Code structure with snippets of code

+ Yep, we'll be needing that for plotting

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

<div align="right">
  <a href="https://github.com/scraptechguy/twet/blob/main/docs/CONCEPTS.md#key-concepts">^</a>
</div>
