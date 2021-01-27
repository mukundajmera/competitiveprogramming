# User function Template for python3

'''
Your task is to complete the merge function which is
used in the mergeSort function as below:
def mergeSort (arr, l, r):
    if l < r:
        m = l + (r - l)/2

        mergeSort (arr, l, m)
        mergeSort (arr, m+1, r)
        merge (arr, l, m, r)
'''


# The first Array is : arr[l...m]
# The Second Array is : arr[m+1...r]

def merge(arr, l, m, r):
    # add code here
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    # initialize 2 variables
    i = 0
    j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:  # left[i] > right[j]:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


# {
#  Driver Code Starts
# Initial Template for Python 3

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        mergeSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends