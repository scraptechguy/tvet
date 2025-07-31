import fmodpy

# adapt the path if your Fortran sources move—
# this will build the shadowing module on install
Shadowing = fmodpy.fimport("tvet/Shadowing_fortran90/shadowing.f90")