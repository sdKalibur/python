import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="hello", type=int)

    args = parser.parse_args()
    print("args", args)
    result = fib(args.num)
    print("Here is your fib", result)

if __name__ == '__main__':
    Main()
