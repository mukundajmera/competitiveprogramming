# User function Template for python3

from collections import defaultdict


def Anagrams(words, n):
    dicti = defaultdict(list)
    for i in words:
        dicti[''.join(sorted(i))].append(i)
    ans = []
    print(dicti)
    for key, value in dicti.items():
        ans.append(dicti.get(key))
    return ans


# def Anagrams(words,n):
#     '''
#     words: list of word
#     n:      no of words
#     return : list of group of anagram {list will be sorted in driver code (not word in grp)}
#     '''

#     #code here
#     #map of sum:value
#     group = {}
#     res = []
#     #calculate assci value append result

#     for i in range(n):
#         sum = 0
#         for j in words[i]:
#             sum += ord(j)
#         if sum in group:
#             temp = group[sum]
#             temp.append(words[i])
#             group[sum] = temp
#         else:
#             group[sum] = [words[i]]

#     #iter result in final list
#     for value in group.values():
#         res.append(value)
#     print(res)
#     return res


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        words = input().split()

        ans = Anagrams(words, n)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

# } Driver Code Ends