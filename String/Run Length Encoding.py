#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    prev = arr[0]
    count = 0
    result = ""
    for i in arr:
        if prev == i:
            count += 1
        else:
            result += prev+str(count)
            prev = i
            count = 1
    result += prev+str(count)
    return result



#{
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends