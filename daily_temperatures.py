def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = [] # [temp, index]

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            result[stackIndex] = (i - stackIndex)
        stack.append([temp, i])
    
    return result