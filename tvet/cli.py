#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import numpy as np
import os
import vispy.app
from .core import Asteroid
from PyQt6.QtWidgets import QApplication, QFileDialog

def parse_vector(vec_str):
    return np.array(list(map(float, vec_str.split(','))))

def main():
    parser = argparse.ArgumentParser(description="TVET CLI")
    parser.add_argument("filename", help="Path to OBJ file")
    parser.add_argument('--shininess', default=100, help="Shininess factor for the asteroid surface")
    parser.add_argument('--wireframe-width', default=1, help="Width of the wireframe lines")
    parser.add_argument("--get-geometry", action="store_true", help="Run get_geometry() and print results")
    parser.add_argument("--get-cosines", action="store_true", help="Run get_cosines() and print results")
    parser.add_argument("--get-fluxes", action="store_true", help="Run get_fluxes() and print results")
    parser.add_argument("--interactive-plot", action="store_true", help="Plot the interactive asteroid geometry and light curve")
    parser.add_argument("--scattering", choices=["lambert", "lommel", "hapke"], default="lambert", help="Scattering law to use: lambert, lommel, or hapke (default: lambert)")
    parser.add_argument('--s', type=parse_vector, default=np.array([1,0,0]), help="Incident light vector, e.g. '1,0,0'")
    parser.add_argument('--o', type=parse_vector, default=np.array([0,0,1]), help="Observer vector, e.g. '0,0,1'")
    args = parser.parse_args()

    asteroid = Asteroid(args=args, filename=args.filename)
    asteroid.s = args.s
    asteroid.o = args.o

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    if args.get_geometry:
        asteroid.get_geometry()
        np.savetxt(os.path.join(output_dir, "centers.txt"), asteroid.centers)
        np.savetxt(os.path.join(output_dir, "normals.txt"), asteroid.normals)
        print(f"Centers saved to {output_dir}/centers.txt")
        print(f"Normals saved to {output_dir}/normals.txt")
        print("Number of centers:", len(asteroid.centers))
        print("Number of normals:", len(asteroid.normals))

    if args.get_cosines:
        asteroid.get_cosines(s=args.s, o=args.o)
        print("mu_i:", asteroid.mu_i)
        print("mu_e:", asteroid.mu_e)
        
    if args.get_fluxes:
        asteroid.get_fluxes()
        np.savetxt(os.path.join(output_dir, "phi_i.txt"), asteroid.phi_i)
        np.savetxt(os.path.join(output_dir, "phi_e.txt"), asteroid.phi_e)
        print(f"phi_i saved to {output_dir}/phi_i.txt")
        print(f"phi_e saved to {output_dir}/phi_e.txt")
        print("Total:", asteroid.total)

    if args.interactive_plot:
        asteroid.interactive_plot()
        vispy.app.run()

if __name__ == "__main__":
    main()
