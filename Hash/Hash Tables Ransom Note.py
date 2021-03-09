#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # hashmap approch
    no_of_words = {}
    # add all in hashmap and update counter over magazine
    for word in magazine:
        if word in no_of_words:
            no_of_words[word] += 1
        else:
            no_of_words[word] = 1

    # iterate over note and check
    for word in note:
        if word in no_of_words:
            if no_of_words[word] == 0:
                print("No")
                return
            else:
                no_of_words[word] -= 1
        else:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
