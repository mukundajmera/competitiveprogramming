# User function Template for python3

'''
Function to push element to front
    * dq : dqueue in which element is to be pushed
    * x : element to be pushed
'''


def push_front_pf(dq, x):
    # code here
    dq.appendleft(x)


''' Function to pop element from back
    * dq : dqueue From which element is to be popped
'''


def push_back_pb(dq, x):
    # code here
    dq.append(x)


'''
Function to return element from front
    * dq : dqueue from which element is to be returned
'''


def front_dq(dq):
    # code here
    if len(dq) == 0:
        return -1
    else:
        return dq[0]


'''
 Function to pop element from back
    * dq : dqueue From which element is to be popped

'''


def pop_back_ppb(dq):
    # code here
    if len(dq) != 0:
        return dq.pop()


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    from collections import deque

    tcs = int(input())

    for _ in range(tcs):

        dq = deque()

        n = int(input())

        for _ in range(n):
            qry = input().split()

            if qry[0] == 'pf':
                x = int(qry[1])
                push_front_pf(dq, x)
                print(dq[0])

            elif qry[0] == 'pb':
                x = int(qry[1])
                push_back_pb(dq, x)
                print(dq[-1])

            elif qry[0] == 'pp_b':
                pop_back_ppb(dq)
                print(len(dq))

            else:
                x = front_dq(dq)
                print(x)

# } Driver Code Ends