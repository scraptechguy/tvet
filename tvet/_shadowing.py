# tvet/_shadowing.py

import os
import fmodpy

_this_dir = os.path.dirname(__file__)
_src_dir  = os.path.join(_this_dir, "fortran")

# build absolute paths to all of your .f90 files
main_source = os.path.join(_src_dir, "shadowing.f90")
dependencies = [
    os.path.join(_src_dir, "vector_product.f90"),
    os.path.join(_src_dir, "normalize.f90"),
    os.path.join(_src_dir, "boundingbox.f90"),
    os.path.join(_src_dir, "intersect_AB_t.f90"),
]

Shadowing = fmodpy.fimport(
    main_source,
    dependencies=dependencies,
    verbose=True,
    f_compiler_args="-fPIC -shared -O3",
    output_dir=_src_dir,
)
