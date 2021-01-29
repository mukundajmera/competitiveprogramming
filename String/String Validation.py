# User function Template for python3

"""
input -
s = string given

output -
return 0 if not validated else return true
"""


def validate(s):
    isNumeric = False
    isUpper = False
    isLower = False
    isSpecial = False
    isLength = False
    # your code here
    for char in s:
        value = ord(char)
        if value >= 48 and value <= 57:
            isNumeric = True

        if value >= 65 and value <= 90:
            isUpper = True

        if value >= 97 and value <= 122:
            isLower = True

        if char in '@#$-*':
            isSpecial = True

    if len(s) >= 10:
        isLength = True

    if (isNumeric and isUpper and isLower and isSpecial and isLength):
        return 1
    else:
        return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        print(validate(s))
        t = t - 1

# } Driver Code Ends