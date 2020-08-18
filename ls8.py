#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

if len(sys.argv) != 2:
    cpu.load()

else:
    filename = sys.argv[1]
    cpu.load_file(filename)

cpu.run()
