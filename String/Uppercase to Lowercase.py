#User function Template for python3

"""
input -
@s :- string to be converted

output -
return converted string
"""
def caseConversion(s):
   #your code here
   return s.lower()



#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(caseConversion(s))
        t = t-1

# } Driver Code Ends