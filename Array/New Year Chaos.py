#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(Q):
    moves = 0
    Q = [P-1 for P in Q]
    for i,P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            # print(j, Q[j], P)
            if Q[j] > P:
                moves += 1
    print(moves)

#     n = len(q)
#     no_of_bribe = 0
#     for person in range(n-1,-1,-1):
#          person_value = q[person]
#         #  print(person, person_value)
#          if person == person_value:
#             continue
#          elif person_value < person:
#             continue
#          elif person_value > person:
#             #check for difference
#             difference = person_value - person - 1
#             # print(difference,person_value,person)
#             if difference > 2:
#                 print("Too chaotic")
#                 return
#             else:
#                 no_of_bribe += difference
#     print(no_of_bribe)
#     return no_of_bribe
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
