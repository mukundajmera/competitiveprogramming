# from collections import Counter
# def countDistinct(arr, n, k):
#     res = []
#     for i in range(n-k+1):
#         l=arr[i:i+k]
#         res.append(len(Counter(l).keys()))
#     return res
# def countDistinct(arr, N, K):
#     # Code here
#     # freq = {i:arr[:k].count(i) for i in arr[:k]}
#     res = []
#     res.append(len(set(arr[:k])))
#     for i in range(1,n-k+1):
#         res.append(len(set(arr[i:i+k])))

#     return res

def countDistinct(arr, N, K):
    # Code here
    freq = {}
    for i in arr[:k]:
        if freq.get(i) == None:
            freq[i] = 1
        else:
            freq[i] += 1
    res = []
    res.append(len(freq))
    for i in range(1, N - k + 1):
        # decrease freq of old element
        if arr[i - 1] in freq:
            # decrease by one
            freq[arr[i - 1]] -= 1
            # if zero frequency delete
            if freq[arr[i - 1]] == 0:
                del freq[arr[i - 1]]
        if arr[i + k - 1] in freq:
            freq[arr[i + k - 1]] += 1
        else:
            freq[arr[i + k - 1]] = 1
        res.append(len(freq))
    return res


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = countDistinct(arr, n, k)
        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends