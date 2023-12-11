import math

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    result = max(piles)

    while left <= right:
        time = 0
        k = (left + right) // 2
        for p in piles:
            time += math.ceil(p / k)
        
        if time <= h:
            result = min(result, k)
            right = k - 1
        else:
            left = k + 1
    
    return result