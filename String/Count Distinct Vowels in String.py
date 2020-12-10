# User function Template for python3

def countVowels(s):
    # code here
    dist_vowel = set()
    for char in s:
        if char in 'aeiou':
            dist_vowel.add(char)

    return len(dist_vowel)


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