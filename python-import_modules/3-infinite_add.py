#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:  # skip the program name
        total += int(arg)
    print(total)
