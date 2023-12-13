def findMin(nums):
    left, right = 0, len(nums) - 1
    result = nums[0]

    while left <= right:
        if nums[left] < nums[right]:
            result = min(result, nums[left])
        
        medium = (left + right) // 2
        if nums[medium] >= nums[right]:
            left = medium + 1
        else:
            right = medium - 1
    
    return result
