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

def main():
    ele = load_ele("docs/segments/load_ele/tri_file_octdecv_1.1.ele", True)

if __name__ == "__main__": 
    main()