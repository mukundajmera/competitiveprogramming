#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    charArr = [0 for _ in range(26)]
    changes = 0
    # iterate over string using charset array
    a_len = len(a)
    a_iter, b_iter = 0, 0
    b_len = len(b)
    while (a_len > a_iter or b_len > b_iter):
        if a_len > a_iter:
            char = a[a_iter]
            a_iter += 1
            charArr[ord(char) % 97] += 1
        if b_len > b_iter:
            char = b[b_iter]
            b_iter += 1
            charArr[ord(char) % 97] -= 1
    # remaing add over abs
    for char in charArr:
        if char != 0:
            changes += abs(char)

    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
