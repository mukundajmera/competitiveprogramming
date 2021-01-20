# User function Template for python3


# Complete this function
def printNonRepeated(arr, n):
    # Your code here
    array_index = {item: 0 for item in arr}
    result = []

    for i in arr:
        array_index[i] += 1

    for i in arr:
        if array_index[i] == 1:
            result.append(i)

    return result


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        l = printNonRepeated(arr, n)
        print(*l)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends