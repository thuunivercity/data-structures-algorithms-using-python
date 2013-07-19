def inorderTrav(subtree):
    if subtree is not None:
        inorderTrav(subtree.left)
        print (subtree.data)
        inorderTrav(subtree.right)

