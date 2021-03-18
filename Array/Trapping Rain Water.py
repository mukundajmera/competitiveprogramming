
class Solution:
    def trappingWater(self, arr ,n):
        # Code here
        lmax = [0 ] *n
        rmax = [0 ] *n
        result = 0
        # compute lmax
        lmax[0] = arr[0]
        for i in range(1 ,n):
            lmax[i] = max(lmax[ i -1] ,arr[i])

        # compute rmax
        rmax[ n -1] = arr[ n -1]
        for i in range( n -2 ,-1 ,-1):
            rmax[i] = max(arr[i] ,rmax[ i +1])

        for wall in range(1 , n -1):
            # print(min(lmax[wall],rmax[wall]) ,min(lmax[wall],rmax[wall]) - arr[wall])
            result += min(lmax[wall] ,rmax[wall]) - arr[wall]

        return result


# {
#  Driver Code Starts
# Initial Template for Python 3

import math



def main():
    T=int( input())
    while(T>0 ):

        n= int(input())

        arr=[int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.trappingWater(arr,n))
        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends