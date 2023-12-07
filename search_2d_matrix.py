def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bottom = 0, ROWS - 1
    while top <= bottom:
        row = (top + bottom) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break
    
    if not (top <= bottom):
        return False
    
    left, right = 0, COLS - 1
    row = (top + bottom) // 2
    while left <= right:
        medium = (left + right) // 2
        if target > matrix[row][medium]:
            left = medium + 1
        elif target < matrix[row][medium]:
            right = medium - 1
        else:
            return True
    return False