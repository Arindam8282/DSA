def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_frequency = 0
    lp = 0
    max_len = 0
    for rp in range(len(s)):
        if s[rp] in count:
            count[s[rp]] += 1
        else:
            count[s[rp]] = 1
        max_frequency = max(max_frequency,count[s[rp]])
        window_sum = rp-lp+1
        if(window_sum-max_frequency>k):
            count[s[lp]]-=1
            lp+=1
        max_len = max(max_len,rp-lp+1)

    return max_len
print(characterReplacement("ABAB",2))
print(characterReplacement("AABABBA",1))
print(characterReplacement("AABABBA",2))

        