#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    preComputer = {}
    preComputer[0], preComputer[1] = arr[0], max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        preComputer[i] = max(preComputer[i - 1], preComputer[i - 2] + num, preComputer[i - 2], num)
    return preComputer[len(arr) - 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
