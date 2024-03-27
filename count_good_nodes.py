def goodNodes(root):

    def dfs(node, maxVal):
        if not node:
            return 0
        
        result = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        result += dfs(node.left, maxVal)
        result += dfs(node.right, maxVal)
        return result
    
    return dfs(root, root.val)