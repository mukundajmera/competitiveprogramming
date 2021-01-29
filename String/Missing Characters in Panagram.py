# User function Template for python3

"""
input -
@s = given string

output -
return -1 or required ans
"""


def missingPanagram(s):
    char_set = [0] * 256
    missing_char = ''

    for i in s.lower():
        char_set[ord(i)] += 1

    for i in range(97, 123):
        if char_set[i] == 0:
            missing_char = missing_char + chr(i)

    return missing_char


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        print(missingPanagram(s))
        t = t - 1

# } Driver Code Ends