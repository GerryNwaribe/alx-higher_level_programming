#!/usr/bin/python3
import sys
a = len(sys.argv) - 1
print("{} {}:".format(a, a == 1 and "argument" or "arguments"))
for b, arg in enumerate(sys.argv[:1], 1):
    print("{}: {}".format(b, arg))
