def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    seen = {}
    for i in range(len(s)):
        if s[i] not in seen:
            seen[s[i]] = 1
        else:
            seen[s[i]] += 1        
    for i in t:
        if i in seen and seen[i]-1>=0:
            seen[i] -= 1
        else:
            return False
    return True
print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))
print(isAnagram("xa","xx"))
print(isAnagram("aacc","ccac"))


