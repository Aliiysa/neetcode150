from collections import deque

def rightSideView(root):
    q = deque([root])
    result = []

    while q:
        rightSide = None
        qLen = len(q)
        for i in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            result.append(rightSide.val)
    return result