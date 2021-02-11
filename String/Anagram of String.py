# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
from collections import defaultdict


def remAnagram(str1, str2):
    # add code here
    charSet = defaultdict(int)
    pos1 = pos2 = 0
    while pos1 < len(str1) or pos2 < len(str2):
        if pos1 < len(str1):
            charSet[str1[pos1]] += 1
            # print(str1[pos1],end="")
            pos1 += 1
        if pos2 < len(str2):
            charSet[str2[pos2]] -= 1
            # print(str2[pos2])
            pos2 += 1
    count = 0
    # print(charSet)
    for i in charSet.values():
        if i != 0:
            count += abs(i)
    return count


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        str2 = input()
        print(remAnagram(str1, str2))
# } Driver Code Ends