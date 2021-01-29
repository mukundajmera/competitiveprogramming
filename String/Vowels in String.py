# User function Template for python3

def countVowels(s):
    # code here
    count = 0
    for i in s:
        if i.lower() in 'aeiou':
            count += 1

    return count


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        s = input()

        print(countVowels(s))
# } Driver Code Ends