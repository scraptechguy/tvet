#!/usr/bin/env python3

def load_ele(filename, debug=False): 
    '''Load an ELE file.'''
    
    ele = []

    f = open(filename, "r")

    for line in f.readlines()[1:]:
        if len(line) == 0:
            continue
        elif line[0] == '#': 
            continue

        l = line.split()
        l = l[1:]

        ele.append(l)

    f.close

    if debug:
        print("number of elements = " + str(len(ele)) + ", beginning with element " + str(ele[0]))

def load_node(filename, debug=False): 
    '''Load an NODE file.'''
    
    node = []

    f = open(filename, "r")

    for line in f.readlines()[1:]:
        if len(line) == 0:
            continue
        elif line[0] == '#': 
            continue

        l = line.split()
        l = l[1:]

        node.append(l)

    f.close()

    if debug:
        print("number of nodes = " + str(len(node)) + ", beginning with node " + str(node[0]))

def load_face(filename, debug=False): 
    '''Load an FACE file.'''

    face = []
    
    f = open(filename, "r")

    for line in f.readlines()[1:]:
        if len(line) == 0:
            continue
        elif line[0] == '#': 
            continue

        l = line.split()
        l = l[1:4]

        face.append(l)

    f.close()

    if debug:
       print("number of faces = " + str(len(face)) + ", beginning with face " + str(face[0]))

def load_obj(filename, debug=False):
    '''Load a Wavefront OBJ file.''' 
    
    node = []
    face = []

    f = open(filename, "r")

    for line in f.readlines(): 
        if len(line) == 0:
            continue
        elif line[0] == '#': 
            continue

        l = line.split()
        
        if l[0] == 'v':
            node.append(list(map(float, l[1:])))
        elif l[0] == 'f':
            face.append(list(map(lambda x: int(x) - 1, l[1:])))

    f.close()

    if debug:
        print("number of nodes = " + str(len(node)) + ", beginning with node " + str(node[0]))
        print("number of faces = " + str(len(face)) + ", beginning with face " + str(face[0]))

    return node, face


def main():
    ele = load_ele("src/sample_files/tri_file_octdecv_1.1.ele", True)
    # node = load_node("src/sample_files/tri_file_octdecv_1.1.node", True)
    # face = load_face("src/sample_files/tri_file_octdecv_1.1.face", True)
    # obj_node, obj_face = load_obj("src/sample_files/tri_file_octdecv_1.obj", True)

if __name__ == "__main__": 
    main()
