# {
# Driver Code Starts
# Initial Template for Python 3


stackMax = 100000
stack = [-1] * stackMax
top = -1

# } Driver Code Ends

# User function Template for python3
stack = []


##Complete these functions
def push(data):
    ##Your code here
    global top
    top_value = top
    if top_value == 100000:
        print('Stack Full')
    else:
        top = top_value + 1
        stack.append(data)


def pop():
    ##Your code here
    global top
    top_value = top
    if top_value == -1:
        print("Stack Empty")
    else:
        top = top_value - 1
        stack.pop()


def display():
    ##Your code here
    global top
    global stack
    stacks = stack
    top_value = top
    # print('top value',stacks)
    if top_value == -1:
        print(-1)
    else:
        print(*stacks)


# {
# Driver Code Starts.


def main():
    global top
    testcases = int(input())
    while (testcases > 0):
        top = -1
        queries = int(input())
        while (queries > 0):

            queryType = input()

            if (queryType[0] == '1'):

                x = int(queryType[2])
                push(x)

            elif (queryType[0] == '2'):
                pop()

            else:
                display()

            queries -= 1

        testcases -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
