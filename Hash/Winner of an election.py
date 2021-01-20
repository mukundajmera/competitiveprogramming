# User function Template for python3

# Complete this function

def winner(arr, n):
    # Your code here
    # return the name of the winning candidate and the votes he recieved
    winners = []
    participants = {item: 0 for item in arr}
    for i in arr:
        participants[i] = participants[i] + 1

    winner_votes = max(participants.values())
    for key, value in participants.items():
        if value == winner_votes:
            winners.append(key)
    winners.sort()
    return (winners[0], winner_votes)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = input().strip().split()

        result = winner(arr, n)
        print(result[0], result[1])
# } Driver Code Ends