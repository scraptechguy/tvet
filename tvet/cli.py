#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from .core import Asteroid

def main():
    parser = argparse.ArgumentParser(description="TVET CLI")
    parser.add_argument("filename", help="Path to OBJ file")
    parser.add_argument('--shininess', default=100, help="Shininess factor for the asteroid surface")
    parser.add_argument('--wireframe-width', default=1, help="Width of the wireframe lines")
    parser.add_argument("--get-cosines", action="store_true", help="Run get_cosines() and print results")
    args = parser.parse_args()

    asteroid = Asteroid(args=args, filename=args.filename)
    if args.get_cosines:
        asteroid.get_cosines()
        print("mu_i:", asteroid.mu_i)
        print("mu_e:", asteroid.mu_e)

if __name__ == "__main__":
    main()
