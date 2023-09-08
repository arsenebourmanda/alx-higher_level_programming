#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    mySum = 0
    for a in range(len(sys.argv) - 1):
        mySum = mySum + int(sys.argv[a + 1])
    print(mySum)

