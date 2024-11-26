#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import fmodpy
import tkinter
import tkinter.filedialog
import numpy as np
import vispy
import vispy.app
import vispy.scene
import vispy.visuals
import vispy.io
import vispy.gloo

import Load
import Hapke

Shadowing = fmodpy.fimport("src/Shadowing/shadowing.f90")