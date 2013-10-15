#!/usr/bin/env python3

import sys

from tbar.tbar import TBar

def main(infile=None, _max=0, length=0, vertical=False):
    infile = infile or sys.stdin
    b = TBar(infile, _max=_max, length=length, vertical=vertical)
    print(str(b))
    return
