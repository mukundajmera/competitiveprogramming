#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    if len(arr[0]) < 3 or len(arr) < 3:
        return 0
    else:
        max_sum = -math.inf
        for row in range(0,len(arr)-2):
            for col in range(0,len(arr)-2):
                row1 = arr[row][col] + arr[row][col+1] + arr[row][col+2]
                row2 = arr[row+1][col+1]
                row3 = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
                # print(row1, row2, row3)
                max_sum = max(max_sum,row1 + row2 + row3)
        return max_sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
