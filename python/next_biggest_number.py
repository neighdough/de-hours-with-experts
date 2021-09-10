#!/usr/bin/python3
import sys
from itertools import permutations

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    stnum = str(num)
    all_combo = sorted([int(''.join(i)) for i in list(permutations(list(stnum)))])
    for v in all_combo:
        if v > int(num):
            return v
    return -1

if __name__ == "__main__":
    main()



