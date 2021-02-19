# User function Template for python3
def maximumMeetings(n, start, end):
    # code here
    activity = []
    max_meeting = 1
    # add activity
    for meeting in range(n):
        activity.append((start[meeting], end[meeting]))
    # sort them based on meeting end
    activity.sort(key=lambda key: key[1])
    activtiy_start, activity_end = activity[0][0], activity[0][1]
    for i in range(1, n):
        if activity_end < activity[i][0]:
            max_meeting += 1
            activity_end = activity[i][1]

    # print(activity)
    return max_meeting


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        print(maximumMeetings(n, start, end))
# } Driver Code Ends