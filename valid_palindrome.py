def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while not isAlphaNum(s[left]) and left < right:
            left += 1
        while not isAlphaNum(s[right]) and left < right:
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def isAlphaNum(c):
    return (ord("a") <= ord(c) <= ord("z")
            or ord("A") <= ord(c) <= ord("Z")
            or ord("0") <= ord(c) <= ord("9"))