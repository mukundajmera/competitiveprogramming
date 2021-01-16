# User function Template for python3

'''
@Node structure -
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
'''


def preOrder(root):
    # code here
    result = []
    # code here
    if not root: return result
    result.append(root.val)
    result.extend(preOrder(root.left))
    result.extend(preOrder(root.right))

    return result


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


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
        res = preOrder(root)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends