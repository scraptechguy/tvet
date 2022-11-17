#!/usr/bin/env python3

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

def main():
    face = load_face("docs/segments/load_face/tri_file_octdecv_1.1.face", True)

if __name__ == "__main__": 
    main()