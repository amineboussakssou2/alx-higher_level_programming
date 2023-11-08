#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    count = 0

    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in sys.argv[1:]:
            len(sys.argv) == 1
            count += 1
            print("{}: {}".format(count, i))

    elif len(sys.argv) > 1:
        print("{} argument:".format(len(sys.argv) - 1))
        print("1: {}".format(sys.argv[1]))

    else:
        print("{} arguments.".format(len(sys.argv) - 1))
