# User function Template for python3

'''
@node template -
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
'''
from collections import deque


def levelOrder(root):
    # code here
    result = []
    stack = deque()
    if root == None:
        return result
    else:
        stack.append(root)
        while len(stack) > 0:
            node = stack.popleft()
            result.append(node.val)

            # check left
            if node.left != None:
                stack.append(node.left)
            # check right
            if node.right != None:
                stack.append(node.right)
        return result


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def insert(root, node):
    if root == None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


if __name__ == "__main__":
    t = int(input())
    for ti in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        root = Node(arr[0])
        for i in range(1, n):
            insert(root, Node(arr[i]))
        res = levelOrder(root)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends