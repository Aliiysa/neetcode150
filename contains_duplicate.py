def containsDuplicate(nums):
    hash = {}
    for i in nums:
        if i in hash:
            return True
        hash[i] = 1 + hash.get(i, 0)
    return False

print(containsDuplicate([1,2,3,1]))