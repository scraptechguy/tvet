'''This Python code is an automatically generated wrapper
for Fortran code made by 'fmodpy'. The original documentation
for the Fortran source code follows.

! shadowing.f90
! Shadowing, non-convex version.
! Miroslav Broz (miroslav.broz@email.cz), Oct 26th 2022
'''

import os
import ctypes
import platform
import numpy

# --------------------------------------------------------------------
#               CONFIGURATION
# 
_verbose = True
_fort_compiler = "gfortran"
_shared_object_name = "shadowing." + platform.machine() + ".so"
_this_directory = os.path.dirname(os.path.abspath(__file__))
_path_to_lib = os.path.join(_this_directory, _shared_object_name)
_compile_options = ['-fPIC', '-shared', '-O3']
_ordered_dependencies = ['shadowing.f90', 'vector_product.f90', 'normalize.f90', 'boundingbox.f90', 'intersect_AB_t.f90', 'shadowing_c_wrapper.f90']
_symbol_files = []# 
# --------------------------------------------------------------------
#               AUTO-COMPILING
#
# Try to import the prerequisite symbols for the compiled code.
for _ in _symbol_files:
    _ = ctypes.CDLL(os.path.join(_this_directory, _), mode=ctypes.RTLD_GLOBAL)
# Try to import the existing object. If that fails, recompile and then try.
try:
    # Check to see if the source files have been modified and a recompilation is needed.
    if (max(max([0]+[os.path.getmtime(os.path.realpath(os.path.join(_this_directory,_))) for _ in _symbol_files]),
            max([0]+[os.path.getmtime(os.path.realpath(os.path.join(_this_directory,_))) for _ in _ordered_dependencies]))
        > os.path.getmtime(_path_to_lib)):
        print()
        print("WARNING: Recompiling because the modification time of a source file is newer than the library.", flush=True)
        print()
        if os.path.exists(_path_to_lib):
            os.remove(_path_to_lib)
        raise NotImplementedError(f"The newest library code has not been compiled.")
    # Import the library.
    clib = ctypes.CDLL(_path_to_lib)
except:
    # Remove the shared object if it exists, because it is faulty.
    if os.path.exists(_shared_object_name):
        os.remove(_shared_object_name)
    # Compile a new shared object.
    _command = [_fort_compiler] + _ordered_dependencies + _compile_options + ["-o", _shared_object_name]
    if _verbose:
        print("Running system command with arguments")
        print("  ", " ".join(_command))
    # Run the compilation command.
    import subprocess
    subprocess.check_call(_command, cwd=_this_directory)
    # Import the shared object file as a C library with ctypes.
    clib = ctypes.CDLL(_path_to_lib)
# --------------------------------------------------------------------


class shadowing_module:
    '''! Dicrectional cosine.'''

    
    # ----------------------------------------------
    # Wrapper for the Fortran subroutine MU
    
    def mu(self, normals, s, mu_i):
        ''''''
        
        # Setting up "normals"
        if ((not issubclass(type(normals), numpy.ndarray)) or
            (not numpy.asarray(normals).flags.f_contiguous) or
            (not (normals.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'normals' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            normals = numpy.asarray(normals, dtype=ctypes.c_double, order='F')
        normals_dim_1 = ctypes.c_long(normals.shape[0])
        normals_dim_2 = ctypes.c_long(normals.shape[1])
        
        # Setting up "s"
        if ((not issubclass(type(s), numpy.ndarray)) or
            (not numpy.asarray(s).flags.f_contiguous) or
            (not (s.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 's' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            s = numpy.asarray(s, dtype=ctypes.c_double, order='F')
        s_dim_1 = ctypes.c_long(s.shape[0])
        
        # Setting up "mu_i"
        if ((not issubclass(type(mu_i), numpy.ndarray)) or
            (not numpy.asarray(mu_i).flags.f_contiguous) or
            (not (mu_i.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'mu_i' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            mu_i = numpy.asarray(mu_i, dtype=ctypes.c_double, order='F')
        mu_i_dim_1 = ctypes.c_long(mu_i.shape[0])
    
        # Call C-accessible Fortran wrapper.
        clib.c_mu(ctypes.byref(normals_dim_1), ctypes.byref(normals_dim_2), ctypes.c_void_p(normals.ctypes.data), ctypes.byref(s_dim_1), ctypes.c_void_p(s.ctypes.data), ctypes.byref(mu_i_dim_1), ctypes.c_void_p(mu_i.ctypes.data))
    
        # Return final results, 'INTENT(OUT)' arguments only.
        return mu_i

    
    # ----------------------------------------------
    # Wrapper for the Fortran subroutine NON
    
    def non(self, mu_i, mu_e, nu_i, nu_e):
        ''''''
        
        # Setting up "mu_i"
        if ((not issubclass(type(mu_i), numpy.ndarray)) or
            (not numpy.asarray(mu_i).flags.f_contiguous) or
            (not (mu_i.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'mu_i' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            mu_i = numpy.asarray(mu_i, dtype=ctypes.c_double, order='F')
        mu_i_dim_1 = ctypes.c_long(mu_i.shape[0])
        
        # Setting up "mu_e"
        if ((not issubclass(type(mu_e), numpy.ndarray)) or
            (not numpy.asarray(mu_e).flags.f_contiguous) or
            (not (mu_e.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'mu_e' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            mu_e = numpy.asarray(mu_e, dtype=ctypes.c_double, order='F')
        mu_e_dim_1 = ctypes.c_long(mu_e.shape[0])
        
        # Setting up "nu_i"
        if ((not issubclass(type(nu_i), numpy.ndarray)) or
            (not numpy.asarray(nu_i).flags.f_contiguous) or
            (not (nu_i.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'nu_i' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            nu_i = numpy.asarray(nu_i, dtype=ctypes.c_double, order='F')
        nu_i_dim_1 = ctypes.c_long(nu_i.shape[0])
        
        # Setting up "nu_e"
        if ((not issubclass(type(nu_e), numpy.ndarray)) or
            (not numpy.asarray(nu_e).flags.f_contiguous) or
            (not (nu_e.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'nu_e' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            nu_e = numpy.asarray(nu_e, dtype=ctypes.c_double, order='F')
        nu_e_dim_1 = ctypes.c_long(nu_e.shape[0])
    
        # Call C-accessible Fortran wrapper.
        clib.c_non(ctypes.byref(mu_i_dim_1), ctypes.c_void_p(mu_i.ctypes.data), ctypes.byref(mu_e_dim_1), ctypes.c_void_p(mu_e.ctypes.data), ctypes.byref(nu_i_dim_1), ctypes.c_void_p(nu_i.ctypes.data), ctypes.byref(nu_e_dim_1), ctypes.c_void_p(nu_e.ctypes.data))
    
        # Return final results, 'INTENT(OUT)' arguments only.
        return nu_i, nu_e

    
    # ----------------------------------------------
    # Wrapper for the Fortran subroutine NU
    
    def nu(self, faces, nodes, normals, centres, s, nu_i):
        ''''''
        
        # Setting up "faces"
        if ((not issubclass(type(faces), numpy.ndarray)) or
            (not numpy.asarray(faces).flags.f_contiguous) or
            (not (faces.dtype == numpy.dtype(ctypes.c_int)))):
            import warnings
            warnings.warn("The provided argument 'faces' was not an f_contiguous NumPy array of type 'ctypes.c_int' (or equivalent). Automatically converting (probably creating a full copy).")
            faces = numpy.asarray(faces, dtype=ctypes.c_int, order='F')
        faces_dim_1 = ctypes.c_long(faces.shape[0])
        faces_dim_2 = ctypes.c_long(faces.shape[1])
        
        # Setting up "nodes"
        if ((not issubclass(type(nodes), numpy.ndarray)) or
            (not numpy.asarray(nodes).flags.f_contiguous) or
            (not (nodes.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'nodes' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            nodes = numpy.asarray(nodes, dtype=ctypes.c_double, order='F')
        nodes_dim_1 = ctypes.c_long(nodes.shape[0])
        nodes_dim_2 = ctypes.c_long(nodes.shape[1])
        
        # Setting up "normals"
        if ((not issubclass(type(normals), numpy.ndarray)) or
            (not numpy.asarray(normals).flags.f_contiguous) or
            (not (normals.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'normals' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            normals = numpy.asarray(normals, dtype=ctypes.c_double, order='F')
        normals_dim_1 = ctypes.c_long(normals.shape[0])
        normals_dim_2 = ctypes.c_long(normals.shape[1])
        
        # Setting up "centres"
        if ((not issubclass(type(centres), numpy.ndarray)) or
            (not numpy.asarray(centres).flags.f_contiguous) or
            (not (centres.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'centres' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            centres = numpy.asarray(centres, dtype=ctypes.c_double, order='F')
        centres_dim_1 = ctypes.c_long(centres.shape[0])
        centres_dim_2 = ctypes.c_long(centres.shape[1])
        
        # Setting up "s"
        if ((not issubclass(type(s), numpy.ndarray)) or
            (not numpy.asarray(s).flags.f_contiguous) or
            (not (s.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 's' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            s = numpy.asarray(s, dtype=ctypes.c_double, order='F')
        s_dim_1 = ctypes.c_long(s.shape[0])
        
        # Setting up "nu_i"
        if ((not issubclass(type(nu_i), numpy.ndarray)) or
            (not numpy.asarray(nu_i).flags.f_contiguous) or
            (not (nu_i.dtype == numpy.dtype(ctypes.c_double)))):
            import warnings
            warnings.warn("The provided argument 'nu_i' was not an f_contiguous NumPy array of type 'ctypes.c_double' (or equivalent). Automatically converting (probably creating a full copy).")
            nu_i = numpy.asarray(nu_i, dtype=ctypes.c_double, order='F')
        nu_i_dim_1 = ctypes.c_long(nu_i.shape[0])
    
        # Call C-accessible Fortran wrapper.
        clib.c_nu(ctypes.byref(faces_dim_1), ctypes.byref(faces_dim_2), ctypes.c_void_p(faces.ctypes.data), ctypes.byref(nodes_dim_1), ctypes.byref(nodes_dim_2), ctypes.c_void_p(nodes.ctypes.data), ctypes.byref(normals_dim_1), ctypes.byref(normals_dim_2), ctypes.c_void_p(normals.ctypes.data), ctypes.byref(centres_dim_1), ctypes.byref(centres_dim_2), ctypes.c_void_p(centres.ctypes.data), ctypes.byref(s_dim_1), ctypes.c_void_p(s.ctypes.data), ctypes.byref(nu_i_dim_1), ctypes.c_void_p(nu_i.ctypes.data))
    
        # Return final results, 'INTENT(OUT)' arguments only.
        return nu_i

shadowing_module = shadowing_module()

