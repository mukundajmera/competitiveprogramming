# Sort the array using insertion sort
def insert(arr):
    # add code here
    for i in range(len(arr)):
        ele = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > ele:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = ele

    # {


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        insert(arr)

        for i in range(n):
            print(arr[i], end=" ")

        print()
# } Driver Code Ends