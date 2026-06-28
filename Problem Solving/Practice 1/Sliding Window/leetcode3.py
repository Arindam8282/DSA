def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    left = 0
    hasChar = {}
    for r in range(len(s)):
        while s[r] in hasChar:
            del hasChar[s[left]]
            left += 1
        curlength = r - left + 1
        hasChar[s[r]] = 1
        if max_length < curlength:
            max_length = curlength
    return max_length
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbb"))
print(lengthOfLongestSubstring("pwwkew"))


        
