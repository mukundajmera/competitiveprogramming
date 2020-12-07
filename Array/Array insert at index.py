# User function Template for python3

'''You need to insert the given element at the given index.
After inserting the elements at index, elements
from index onward should be shifted one position ahead
 You may assume that the array already has sizeOfArray - 1
elements.'''


def insertAtIndex(arr, sizeOfArray, index, element):
    # Your code here
    arr.insert(index, element)
    return arr


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        sizeOfArray = int(input())
        arr = [int(x) for x in input().strip().split()]
        arr.append(-1)
        index, element = map(int, input().strip().split())

        insertAtIndex(arr, sizeOfArray, index, element)

        for i in range(sizeOfArray):
            print(arr[i], end=" ")
        print()
        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends