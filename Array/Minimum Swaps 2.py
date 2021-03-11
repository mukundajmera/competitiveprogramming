#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0
    visited = { i:False for i in range(len(arr))}
    for i in range(len(arr)):
        if (visited[i] == False):
            one = i
            two = arr[i] -1
            length = 1
            visited[i] = True
            while(two != i):
                visited[two] = True
                one = two
                two = arr[two] -1
                length += 1
            swap += length-1
        # if arr[i] != i+1:
        #     t = i + 1
        #     while(arr[t] != i + 1):
        #         t += 1
        #     # print(arr)
        #     arr[i], arr[t] = arr[t], arr[i]
        #     swap += 1
    return swap
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
