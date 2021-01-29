#User function Template for python3

"""
input -
s - given string

output -
return 0 if not panagram else return 1
"""
def isPanagram(s):
    #your code here
    char_set = [0]*256

    for i in s.lower():
        char_set[ord(i)] += 1

    for i in range(97,123):
        if char_set[i] == 0:
            return 0

    return 1

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(isPanagram(s))
        t = t-1

# } Driver Code Ends