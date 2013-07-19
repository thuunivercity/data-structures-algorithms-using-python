def preorderTrav(subtree):
    if subtree is not None:
        print(subtree.data)
        preorderTrav(subtree.left)
        preorderTrav(sbutree.right)

