def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for i in nums:
        count[i] = 1 + count.get(i, 0)
    
    for i, c in count.items():
        freq[c].append(i)
    
    result = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result    
