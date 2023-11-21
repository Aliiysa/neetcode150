def isValid(s):
    parentheses = {"]": "[",
            "}": "{",
            ")": "("}
    stack = []

    for c in s:
        if c not in parentheses.keys():
            stack.append(c)
            continue
        if stack and stack[-1] == parentheses[c]:
            stack.pop()
        else:
            return False
    return not stack