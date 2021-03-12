# Enter your code here. Read input from STDIN. Print output to STDOUT
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the commonChild function below.
# def commonChild(s1, s2):
#     pass

def commonChild(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    table = [[0] * (s1_len + 1) for x in range(s2_len + 1)]
    for row in range(1, s2_len + 1):
        for col in range(1, s1_len + 1):
            # making first row and column to zero
            if row == 0 or col == 0:
                table[row][col] = 0
            # if match
            elif s2[row - 1] == s1[col - 1]:
                # take diagonal element
                table[row][col] = 1 + table[row - 1][col - 1]
            # if not match
            else:
                # take maimum of rowMajor or colMajor
                table[row][col] = max(table[row - 1][col], table[row][col - 1])

    return table[s2_len][s1_len]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
