#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1
    if a < 1:
        print("{} arguments.".format(a))
    else:
        print("{} {}:".format(a, a == 1 and "argument" or "arguments"))
        for b, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(b, arg))
