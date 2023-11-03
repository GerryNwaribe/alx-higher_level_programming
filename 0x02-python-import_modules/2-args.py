#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1
    if a == 0:
        print("{}".format('.'))
    else:
        print("{} {}:".format(a, a == 1 and "argument" or "arguments"))
    for b, arg in enumerate(sys.argv[:1], 1):
        print("{}: {}".format(b, arg))
