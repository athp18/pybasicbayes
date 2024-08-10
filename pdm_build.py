# eg. see https://backend.pdm-project.org/hooks/#call-setup-function-to-build-extensions
import os
from Cython.Build import cythonize
import numpy

ext_modules = cythonize(os.path.join('pybasicbayes','util','cstats.pyx'))

def pdm_build_update_setup_kwargs(context, setup_kwargs):
    setup_kwargs.update(
        ext_modules=ext_modules,
        include_dirs=[numpy.get_include()]
    )