# your task is to complete this function
# function should return an integer
def atoi(string):
    # Code here
    for i in string:
        # print(ord(i))
        if ord(i) != 45 and ord(i) < 47 or ord(i) > 57:
            return -1
    return int(string)



#{
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        print(atoi(string))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends