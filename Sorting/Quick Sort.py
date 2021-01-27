# User function Template for python3


'''
parition() function is called as follows:

   def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
'''

'''
This function takes last element as pivot, places  the pivot element 
at its correct position in sorted  array, and places all smaller (smaller
than pivot) to left of pivot and all greater elements to right  of pivot
'''


def partition(arr, low, high):
    # add code here
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # print("pivot before",pivot,arr[j],arr[i])
            arr[j], arr[i] = arr[i], arr[j]
        # print("pivot after",pivot,arr[j],arr[i])

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # print(arr)
    return i + 1


# {
#  Driver Code Starts
# Initial Template for Python 3

def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends