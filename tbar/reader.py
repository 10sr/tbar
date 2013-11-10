#!/usr/bin/env python3

class Reader():
    def __init__(self, infile, comment="#", sep=" ", field=(0,1), regexp=None):
        self.infile = infile
        self.comment = comment
        self.sep = sep
        self.field = field
        self.regexp = regexp
        return

    @property
    def data(self):
        for line in self.infile:
            pair = self.__read_line(line)
            if pair is not None:
                yield pair
        raise StopIteration
        return

    def __read_line(self, line):
        line = line.strip()
        if self.comment and line.startswith(self.comment):
            return None
        elems = line.split(self.sep)
        key = elems[self.field[0]].strip()
        value = elems[self.field[1]].strip()
        if len(value) == 0:
            return (key, 0)
        value = float(value)
        return (key, value)
