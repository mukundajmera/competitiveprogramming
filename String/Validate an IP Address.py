# User function Template for python3

def isValid(s):
    # code here
    parts = s.split(".")
    if len(parts) != 4:
        return False
    for value in parts:
        if value.isdigit():
            if int(value) > 255 or int(value) < 0 or (value[0] == '0' and len(value) != 1):
                return False
        else:
            return False

    return True


# def isValid(s):
#     if s.count('.')!=3:
#         return 0
#     s1=s.split('.')
#     for i in s1:
#         if not i.isdigit() or int(i)<0 or int(i)>255 or (i[0]=='0' and len(i)!=1):
#             return 0
#     return 1


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        if (isValid(s)):
            print(1)
        else:
            print(0)

# } Driver Code Ends