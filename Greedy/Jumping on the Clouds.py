#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    iteration = 0
    while (iteration < len(c) - 1):
        if c[iteration] == 0:
            iteration += 2
        else:
            iteration += 1
        count += 1
        # print(c[iteration], iteration, count)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
