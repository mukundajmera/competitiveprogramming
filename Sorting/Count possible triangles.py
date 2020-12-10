# User function Template for python3

class Solution:

    def findNumberOfTriangles(ob, arr, n):
        arr.sort()
        count = 0

        # traversing through the array elements
        for i in range(n - 2):
            k = i + 2
            for j in range(i + 1, n):
                while (k < n and arr[i] + arr[j] > arr[k]):
                    k += 1
                    count += k - j - 1
        return count
    # def findNumberOfTriangles(ob, arr, n):
    #     #code here
    #     #sort array first
    #     arr.sort()
    #     posibilites = 0
    #     for i in range(n-2):
    #         #two pointer approch
    #         a = i+1
    #         b = n-1
    #         while(b>=i+1):
    #             if arr[a]+arr[i] > arr[b]:
    #                 # print(b,a)
    #                 posibilites = posibilites + (b-a)
    #                 b -= 1
    #                 a = i + 1
    #             else:
    #                 a += 1
    #                 if a == b:
    #                     a = i + 1
    #                     b -= 1
    #     return posibilites


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findNumberOfTriangles(arr, n))

# } Driver Code Ends