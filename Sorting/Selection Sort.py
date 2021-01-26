#User function Template for python3

def select(arr, i):
    # code here
    #done using for loop also
    i =0
    while i < len(arr):
        min_index = i
        j = i+1
        while j < len(arr):
            if arr[min_index] > arr[j]:
                min_index=j
            j = j+1
        return min_index

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1,0, -1):
        j = select(arr,i)

        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp











#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        selectionSort(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends