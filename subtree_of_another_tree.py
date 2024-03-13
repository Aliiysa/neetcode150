def isSubtree(root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False
    if sameTree(root, subRoot):
        return True
    return (isSubtree(root.left, subRoot) or
            isSubtree(root.right, subRoot))

def sameTree(root, subRoot):
    if not root and not subRoot:
        return True
    if root and subRoot and root.val == subRoot.val:
        return (sameTree(root.left, subRoot.left) and
                sameTree(root.right, subRoot.right))
    return False