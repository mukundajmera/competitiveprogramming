def ceil(root,key):
    res = None
    while root != None:
        if root.data == key:
            return root
        elif root.data < key:
            root = root.right
        elif root.data > key:
            res = root
            root = root.right
        return res
