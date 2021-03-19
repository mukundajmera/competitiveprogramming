#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def balance(element, opening):
    if element == ']' and opening == '[' or \
            element == '}' and opening == '{' or \
            element == ')' and opening == '(':
        return True
    else:
        return False


def isBalanced(s):
    # using stack approck
    result = "YES"
    stack = []
    for bracket in s:
        if bracket in '[{(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                result = "NO"
                break
            else:
                open_bracket = stack.pop()
                if balance(bracket, open_bracket) == False:
                    result = "NO"
                    break
    if len(stack) != 0:
        result = "NO"

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
