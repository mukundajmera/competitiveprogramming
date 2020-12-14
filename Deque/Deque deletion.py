# User function Template for python3

def eraseAt(deq, x):
    # code here
    deq.remove(deq[x])


def eraseInRange(deq, s, e):
    # code here
    item = e - s
    for i in range(len(deq)):
        if i >= s and item > 0:
            del deq[s]
            item -= 1


def eraseAll(deq):
    # code here
    deq.clear()


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':

    from collections import deque

    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        qry = input().split()

        deq = deque(arr)

        if int(qry[0]) == 1:

            x = int(qry[1])
            eraseAt(deq, x)

        elif int(qry[0]) == 2:

            start, end = int(qry[1]), int(qry[2])
            eraseInRange(deq, start, end)

        else:
            eraseAll(deq)

        if not deq:
            print('Empty')
        else:
            print(*deq)

# } Driver Code Ends