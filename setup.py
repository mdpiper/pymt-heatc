#! /usr/bin/env python
import os
import sys
import numpy as np

import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension
from model_metadata.utils import get_cmdclass, get_entry_points



common_flags = {
    "include_dirs": [
        np.get_include(),
        os.path.join(sys.prefix, "include"),
    ],
    "library_dirs": [
    ],
    "define_macros": [
    ],
    "undef_macros": [
    ],
    "extra_compile_args": [
    ],
    "language": "c",
}

libraries = [
]

# Locate directories under Windows %LIBRARY_PREFIX%.
if sys.platform.startswith("win"):
    common_flags["include_dirs"].append(os.path.join(sys.prefix, "Library", "include"))
    common_flags["library_dirs"].append(os.path.join(sys.prefix, "Library", "lib"))

ext_modules = [
    Extension(
        "pymt_heatc.lib.heatc",
        ["pymt_heatc/lib/heatc.pyx"],
        libraries=libraries + ["bmiheatc"],
        **common_flags
    ),
]

packages = find_packages()
pymt_components = [(
        "Heatc=pymt_heatc.bmi:Heatc",
        "meta/Heatc",
    ),
]

cmdclass = get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass())

setup(
    name="pymt_heatc",
    author="Mark Piper",
    description="PyMT plugin for heatc",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=cmdclass,
    entry_points=get_entry_points(pymt_components),
)
