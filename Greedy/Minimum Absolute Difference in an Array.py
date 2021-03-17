#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    return min(abs(arr[i + 1] - arr[i]) for i in range(len(arr) - 1))


# def minimumAbsoluteDifference(arr):
#     minimum = math.inf

#     for num in range(len(arr)-1):
#         for pair in range(num+1,len(arr)):
#             # print(arr[num], arr[pair])
#             minimum = min(minimum, abs( arr[num] - arr[pair] ))

#     return minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
