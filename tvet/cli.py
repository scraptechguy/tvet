#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import numpy as np
from .core import Asteroid

def main():
    parser = argparse.ArgumentParser(description="TVET CLI")
    parser.add_argument("filename", help="Path to OBJ file")
    parser.add_argument('--shininess', default=100, help="Shininess factor for the asteroid surface")
    parser.add_argument('--wireframe-width', default=1, help="Width of the wireframe lines")
    parser.add_argument("--get-geometry", action="store_true", help="Run get_geometry() and print results")
    parser.add_argument("--get-cosines", action="store_true", help="Run get_cosines() and print results")
    parser.add_argument("--get-fluxes", action="store_true", help="Run get_fluxes() and print results")
    args = parser.parse_args()

    asteroid = Asteroid(args=args, filename=args.filename)
    if args.get_geometry:
        asteroid.get_geometry()
        np.savetxt("centers.txt", asteroid.centers)
        np.savetxt("normals.txt", asteroid.normals)
        print("Centers:\n", asteroid.centers)
        print("SAVED CENTERS TO centers.txt\n")
        print("Normals:\n", asteroid.normals)
        print("SAVED NORMALS TO normals.txt\n")
        print("Number of centers:", len(asteroid.centers))
        print("Number of normals:", len(asteroid.normals))
    if args.get_cosines:
        asteroid.get_cosines()
        print("mu_i:", asteroid.mu_i)
        print("mu_e:", asteroid.mu_e)
    if args.get_fluxes:
        asteroid.get_fluxes()
        np.savetxt("phi_i.txt", asteroid.phi_i)
        np.savetxt("phi_e.txt", asteroid.phi_e)
        print("phi_i:\n", asteroid.phi_i)
        print("SAVED phi_i TO phi_i.txt\n")
        print("phi_e:\n", asteroid.phi_e)
        print("SAVED phi_e TO phi_e.txt\n")
        print("Total:", asteroid.total)

if __name__ == "__main__":
    main()
