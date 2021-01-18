#User function Template for python3

def left_Rotate_Deq_ByK(deq,k):
    #code here
    while k != 0:
        deq.append(deq[0])
        deq.popleft()
        k -= 1

def right_Rotate_Deq_ByK(deq,k):
    #code here
    while k != 0:
        deq.appendleft(deq[-1])
        deq.pop()
        k -= 1



#{
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        from collections import deque

        n=int(input())
        arr=[int(x) for x in input().split()]
        rTyp,k=[int(x) for x in input().split()]

        deq=deque(arr)

        if rTyp==2:
            left_Rotate_Deq_ByK(deq,k)
        else:
            right_Rotate_Deq_ByK(deq,k)

        print(*deq)
# } Driver Code Ends