def generateParenthesis(n):
    stack = []
    result = []

    def backtrack(openNum, closedNum):
        if openNum == closedNum == n:
            result.append("".join(stack))
            return
        
        if openNum < n:
            stack.append("(")
            backtrack(openNum + 1, closedNum)
            stack.pop()
        
        if closedNum < openNum:
            stack.append(")")
            backtrack(openNum, closedNum + 1)
            stack.pop()
    
    backtrack(0, 0)
    return result
