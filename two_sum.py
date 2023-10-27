def twoSum(nums, target):
    hash = {}

    for i, num in enumerate(nums):
        difference = target - num
        if difference in hash:
            return [hash[difference], i]
        hash[num] = i

