# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

##Complete this function
def sumExists(arr, N, sum):
    ##Your code here
    hash_set = {item: 1 for item in arr}
    for i in arr:
        if hash_set.get(sum - i) and (sum - i) != i:
            return 1
    return 0


# {
# Driver Code Starts.

def main():
    testcases = int(input())
    while (testcases > 0):
        sizeOfArray = int(input())

        arr = [int(x) for x in input().strip().split()]

        sum = int(input())

        print(sumExists(arr, sizeOfArray, sum))

        testcases -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends