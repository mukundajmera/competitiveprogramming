#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    #maximum loose based on sort
    contests.sort(reverse=True,key=lambda x: (x[1],x[0]))
    luck = 0
    for contest in contests:
        points, isImp = contest
        if k > 0 and isImp == 1:
            luck += points
            k -= 1
        elif isImp == 0:
            luck += points
        else:
            luck -= points
    return luck
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
