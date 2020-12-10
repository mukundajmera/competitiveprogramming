# User function Template for python3

##Complete this code
def countNonRepeated(arr, n):
    # Your code here
    counter = {}
    for i in arr:
        if i in counter:
            counter[i] = counter[i] + 1
        else:
            counter[i] = 1
    count = 0
    for key, value in counter.items():
        if value == 1:
            count += 1
    return count


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        print(countNonRepeated(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends