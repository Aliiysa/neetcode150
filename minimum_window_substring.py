def minWindow(s, t):
    if t == "": return ""

    tCount, window = {}, {}
    for c in t:
        tCount[c] = 1 + tCount.get(c, 0)
    
    have, need = 0, len(tCount)
    result, resLen = [-1, -1], float("inf")
    left = 0
    for right in range(len(s)):
        c = s[right]
        window[c] = 1 + window.get(c, 0)

        if window[c] == tCount.get(c, 0):
            have += 1
        
        while have == need:
            # update our result
            if (right - left + 1) < resLen:
                result = [left, right]
                resLen = (right - left + 1)
                # pop from the left of our window
            window[s[left]] -= 1
            if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                have -= 1
            left += 1
            
    left, right = result
    return s[left : right + 1] if resLen != float("inf") else ""