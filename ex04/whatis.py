import sys

try:
    assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
    n = int(sys.argv[1])
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


except ValueError:
    print("AssertionError: argument is not an integer")
except (AssertionError, IndexError) as msg:
    if len(sys.argv) == 1:
        pass
    else:
        print(msg)