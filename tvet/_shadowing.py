import fmodpy

# adapt the path if your Fortran sources move—
# this will build the shadowing module on install
Shadowing = fmodpy.fimport("src/Shadowing/shadowing.f90")