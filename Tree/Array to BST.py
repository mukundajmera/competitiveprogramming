# not working

import math


# node class
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


# main class for generation
class Solution:
    def __init__(self):
        self.result = []

        def sortedArrayToBST(self, nums):
            # Code here
            root = self.arrayToBST(nums)
            self.preOrder(root)
            return self.result

    def arrayToBST(self, arr):

        if not arr:
            return None

        # find middle
        mid = (len(arr) // 2)

        # make the middle element the root
        root = Node(arr[mid])

        # left subtree of root has all
        # values <arr[mid]
        root.left = self.arrayToBST(arr[:mid])

        # right subtree of root has all
        # values >arr[mid]
        root.right = self.arrayToBST(arr[mid + 1:])
        # print(mid)
        return root

        # A utility function to print the preorder

    # traversal of the BST
    def preOrder(self, node):
        if not node:
            return

        self.result.append(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)

    # {


#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.sortedArrayToBST(nums)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends