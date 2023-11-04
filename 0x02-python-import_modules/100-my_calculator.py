#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    a = sys.argv[1:]
    if len(a) != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    c = int(a[0])
    operator = a[1]
    d = int(a[2])
    if operator == '+':
        result = add(c, d)
    elif operator == '-':
        result = sub(c, d)
    elif operator == '*':
        result = mul(c, d)
    elif operator == '/':
        result = div(c, d)
    else:
        print("{}".format('Unknown operator. Available operators: +, -, * and /'))
        exit(1)

print("{} {} {} = {}".format(c, operator, d, result))
