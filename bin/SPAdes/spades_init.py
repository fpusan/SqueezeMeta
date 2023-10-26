#!/usr/bin/env python

############################################################################
# Copyright (c) 2015-2019 Saint Petersburg State University
# Copyright (c) 2011-2014 Saint Petersburg Academic University
# All Rights Reserved
# See file LICENSE for details.
############################################################################

### Modified from SPAdes version 3.15.5
### by Fernando Puente-Sanchez on 2023-JUL-12, for compatibility with the SqueezeMeta pipeline.
### SqueezeMeta is released under the GPL-3 license.

# Change spades_home to match squeezeM directory hierarchy. Fernando Puente-Sanchez, 24-III-2021.

import os
import sys
from os.path import abspath, dirname, realpath, join, isfile

source_dirs = ["", "truspades", "common", "executors", "scripts"]

# developers configuration
spades_home = abspath(dirname(realpath(__file__)))
bin_home = join(spades_home, "bin")
python_modules_home = join(spades_home, "src")
ext_python_modules_home = join(spades_home, "ext", "src", "python_libs")
spades_version = ""


def init():
    global spades_home
    global bin_home
    global python_modules_home
    global spades_version
    global ext_python_modules_home

    # users configuration (spades_init.py and spades binary are in the same directory)
    if isfile(os.path.join(spades_home, "spades-core")):
        install_prefix = dirname(dirname(spades_home)) # FPS: Consider SqueezeMeta dir structure
        bin_home = join(install_prefix, 'bin', 'SPAdes') # FPS: Consider SqueezeMeta dir structure
        spades_home = join(install_prefix, "lib", "spades") # FPS: Consider SqueezeMeta dir structure
        python_modules_home = spades_home
        ext_python_modules_home = spades_home

    for dir in source_dirs:
        sys.path.append(join(python_modules_home, "spades_pipeline", dir))

    spades_version = open(join(spades_home, "VERSION"), 'r').readline().strip()


if __name__ == "__main__":
    spades_py_path = join(dirname(realpath(__file__)), "spades.py")
    sys.stderr.write("Please use " + spades_py_path + " for running SPAdes genome assembler\n")
