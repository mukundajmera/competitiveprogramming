# User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''


def findTree(inorder, preorder, sInd, eInd, preInd, ref):
    if sInd > eInd:
        return None
    root = Node(preorder[preInd[0]])
    preInd[0] += 1
    inIndex = ref.get(root.data)
    # print(inIndex)
    root.left = findTree(inorder, preorder, sInd, inIndex - 1, preInd, ref)
    root.right = findTree(inorder, preorder, inIndex + 1, eInd, preInd, ref)
    return root


def buildtree(inorder, preorder, n):
    preIndex = [0]
    ref = {v: i for i, v in enumerate(inorder)}
    return findTree(inorder, preorder, 0, n - 1, preIndex, ref)


# preIndex = 0
# def buildtree(inorder, preorder, end, start=0):
#     # code here
#     # build tree and return root node
#     global preIndex
#     if start > end:
#         return  None
#     root = Node(preorder[preIndex])
#     preIndex += 1
#     inIndex = None
#     for i in range(start,end):
#         if inorder[i] == root.data:
#             inIndex = i
#             break

#     root.left = buildtree(inorder,preorder,inIndex-1,start)
#     root.right = buildtree(inorder,preorder,end,inIndex+1)
#     return root


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends