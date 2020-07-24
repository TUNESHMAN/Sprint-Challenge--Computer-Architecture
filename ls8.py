#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

if len(sys.argv) != 2:
    # file object that corresponds to the interpreters standard input, output, and error
    print("usage: simple.py filename", file=sys.stderr)
    sys.exit(1)

cpu = CPU()

cpu.load(sys.argv[1])
cpu.run()
