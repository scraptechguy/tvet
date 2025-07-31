#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from PyQt6.QtWidgets import QApplication, QFileDialog
import vispy.app

from .core import Asteroid
from .io import check_filetype

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shininess', default=100)
    parser.add_argument('--wireframe-width', default=1)
    args, _ = parser.parse_known_args()

    app = QApplication([])  
    filename, _ = QFileDialog.getOpenFileName(
        None,
        "Select an OBJ file",
        "",                # start directory
        "OBJ Files (*.obj)"
    )

    # filename = "src/sample_files/tri_file_octdecv_1.obj"
    asteroid = Asteroid(args=args, filename=filename)
    vispy.app.run()

if __name__ == "__main__":
    main()
