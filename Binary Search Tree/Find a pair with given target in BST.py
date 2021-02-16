# User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''


def inorder(root, c=None):
    if c is None:
        c = []
    if root:
        inorder(root.left, c)
        c.append(root.data)
        inorder(root.right, c)
    return c


def isPairPresent(root, target):
    # code here.
    d = {}
    c = inorder(root)
    for i in range(len(c)):
        d[c[i]] = 0
    for i in range(len(c)):
        d[c[i]] += 1
    for key in d:
        try:
            if target == key or (target // 2 == key and target % 2 == 0):
                if d[target - key] >= 2:
                    return 1
                else:
                    return 0
            if d[target - key] >= 1:
                return 1
        except:
            pass
    return 0


# root : the root Node of the given BST
# target : the target sum
# def isPairPresent(root, target):
#     # code here.
#     if root == None:
#         return None
#     left = right = 0
#     found = 0
#     leftVal = rightVal = 0
#     if root.left != None:
#         left = root.left.data
#         leftVal = isPairPresent(root.left,target)
#     if root.right != None:
#         right = root.right.data
#         rightVal = isPairPresent(root.right,target)
#     if ((left + root.data) == target and left != 0 )or\
#         ((right + root.data) == target and right != 0):
#         found = 1
#     return max(found,leftVal,rightVal)

# def isPairPresent(root, target):
#     # code here.
#     res = pairHelper(root,root,target)
#     return 1 if res == True else 0
# def isFind(root,comp):
#     if root==None:
#         return False
#     if root.data<comp:
#         return isfind(root.right,comp)
#     elif root.data >comp:
#         return isFind(root.left,comp)
#     else:
#         return True

# def pairHelper(root,node,target):
#     if node==None:
#         return False
#     lt = pairHelper(root,node.left,target)
#     comp = target-node.data
#     if isFind(root,comp):
#         return True
#     rt = pairHelper(root,node.right,target)
#     return lt or rt

# {
#  Driver Code Starts
# Initial Template for Python 3
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        summ = int(input())
        root = buildTree(s)
        print(isPairPresent(root, summ))
# } Driver Code Ends