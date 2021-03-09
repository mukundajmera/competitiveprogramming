#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    array = {}
    output = []
    #iterate over queries
    for query in queries:
        operation, value  = query
        #add
        if operation == 1:
            array[value] = array.get(value,0) + 1
        #delete
        if operation == 2:
            if array.get(value):
                array[value] -= 1
        #query
        if operation == 3:
            #check frequency
            if value in set(array.values()):
                output.append(1)
            else:
                output.append(0)

    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
