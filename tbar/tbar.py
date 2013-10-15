#!/usr/bin/env python3

class TBar():
    _max = -1
    length = 50
    infile = None
    rawdata = None
    normdata = None
    vertical = False

    def __init__(self, infile, _max=0, length=0, vertical=False):
        self.infile = infile
        if _max:
            self._max = _max
        if length:
            self.length = length
        self.vertical = vertical

        self.rawdata = []
        self.normdata = []

        self.read_input()
        self.set_normdata()
        return

    def __str__(self):
        bars = []
        maxkeylen = max(len(k) for k, v in self.normdata)
        fillspace = " " * maxkeylen
        if self.vertical:
            sep = "-"
        else:
            sep = "|"
        for k, v in self.normdata:
            if self.vertical:
                k = k[::-1]
            bars.append(
                (fillspace + k)[-maxkeylen:] +
                sep +
                ("*" * int(self.length * v) + " " * self.length)[:self.length] +
                sep
            )
        if self.vertical:
            bars = tuple(zip(*bars))
            return str("\n".join("".join(e) for e in reversed(bars)))
        else:
            return str("\n".join(bars))

    def read_input(self):
        for line in self.infile:
            line = line.strip()
            if len(line) == 0 or line.startswith("#"):
                continue
            key, sep, data = line.partition(" ")
            key = key.strip()
            data = data.strip()
            if len(data) == 0:  # no data
                self.rawdata.append((key, 0))
            else:
                self.rawdata.append((key, float(data)))
        return

    def set_max(self):
        self._max = max(tuple(zip(*self.rawdata))[1])
        return self._max

    def set_normdata(self):
        if self._max == -1:
            self.set_max()

        for k, v in self.rawdata:
            self.normdata.append((k, v / self._max))
        return
