def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        medium = (left + right) // 2
        if nums[medium] < target:
            left = medium + 1
        if nums[medium] > target:
            right = medium - 1
        if nums[medium] == target:
            return medium
    return -1
