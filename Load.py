#!/usr/bin/env python3

def load_ele(filename, print_info=True): 
    '''Load an ELE file.'''
    
    f = open(filename, "r")

def load_node(filename, print_info=True): 
    '''Load an NODE file.'''
    
    f = open(filename, "r")

def load_face(filename, print_info=True): 
    '''Load an FACE file.'''
    
    f = open(filename, "r")

def load_obj(filename, print_info=True):
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

    if print_info:
        print("number of nodes = " + str(len(node)) + ", beginning with node " + str(node[0]))
        print("number of faces = " + str(len(face)) + ", beginning with face " + str(face[0]))

    return node, face


def main():
    node, face = load_obj("/Users/rostislavbroz/Downloads/Taky_nevim/tri_file_octdecv_1.obj")

if __name__ == "__main__": 
    main()
