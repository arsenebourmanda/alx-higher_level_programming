#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv)-1) == 0:
        print("{} arguments.".format(len(sys.argv)-1))
    elif (len(sys.argv)-1) == 1:
        print("{} argument:".format(len(sys.argv)-1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        for a in range(len(sys.argv)-1):
            print("{}: {}".format(a+1, sys.argv[a+1]))
