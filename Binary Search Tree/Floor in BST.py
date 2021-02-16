def floor(root,key):
    res = None
    while root != None:
        if root.data == key:
            return root
        elif root.data > key:
            root = root.left
        elif root.data < key:
            res = root
            root = root.left
        return res
