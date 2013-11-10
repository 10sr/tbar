#!/usr/bin/env python3

"""tbar - Terminal Bar

Number to bar in terminal.
"""

__version__ = "0.0.1"

import sys

from tbar.tbar import TBar
from tbar.reader import Reader

def main(infile=None, _max=0, length=0, vertical=False):
    infile = infile or sys.stdin
    r = Reader(infile)
    b = TBar(_max=_max, length=length, vertical=vertical)
    b.add_data_itr(r.data)
    print(str(b))
    return
