#!/usr/bin/env python3

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

        node.append(list(map(float, l[1:])))

    f.close()

    if debug:
        print("number of nodes = " + str(len(node)) + ", beginning with node " + str(node[0]))

def main():
    node = load_node("docs/segments/load_node/tri_file_octdecv_1.1.node", True)

if __name__ == "__main__": 
    main()