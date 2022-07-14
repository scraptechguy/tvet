def load_obj(filename):
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
            face.append(list(map(int, l[1:])))

    return node, face

def main():
    node, face = load_obj("/Users/rostislavbroz/Downloads/Taky_nevim/tri_file_octdecv_1.obj")

    print("number of nodes = " + str(len(node)) + ", beginning with node " + str(node[0]))
    print("number of faces = " + str(len(face)) + ", beginning with face " + str(face[0]))


if __name__ == "__main__": 
    main()
