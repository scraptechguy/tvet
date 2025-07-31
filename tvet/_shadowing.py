# tvet/_shadowing.py

import os
import fmodpy

_this_dir = os.path.dirname(__file__)
_src_dir  = os.path.join(_this_dir, "Shadowing_fortran90")

# build absolute paths to all of your .f90 files
all_sources = [os.path.join(_src_dir, fn) for fn in (
    "shadowing.f90",
    "vector_product.f90",
    "normalize.f90",
    "boundingbox.f90",
    "intersect_AB_t.f90",
    "shadowing_c_wrapper.f90",
)]

# tell fmodpy to compile them all in one shot.
# the first path is the “main” file; the rest become dependencies.
Shadowing = fmodpy.fimport(
    all_sources[0],
    dependencies=all_sources[1:],
    verbose=True,               # optional, to see the exact gfortran command
    f_compiler_args="-fPIC -shared -O3",  # optional flags if you need them
)
