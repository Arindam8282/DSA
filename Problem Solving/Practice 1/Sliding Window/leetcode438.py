def findAnagrams(s: str, p: str) -> [int]:
    lp = 0
    p_counter = {}
    for ch in p:
        if ch not in p_counter:
            p_counter[ch] = 1
        else:
            p_counter[ch]+=1
    window_sum = {}
    outlist = []
    for rp in range(len(s)):
        if window_sum == p_counter:
            outlist.append(lp)
            window_sum[s[lp]] -= 1
            lp += 1

        if s[rp] in window_sum:
            if window_sum[s[rp]] == p_counter[s[rp]]:
                lp = rp
                window_sum = {}
                window_sum[s[rp]] = 1
            else:
                window_sum[s[rp]] += 1
        else:
            if s[rp] in p_counter:
                window_sum[s[rp]] = 1
            else:
                lp+=1
    if window_sum==p_counter:
        outlist.append(lp)
    return outlist

print(findAnagrams("cbaebabacd","abc"))
print(findAnagrams("abab","ab"))
print(findAnagrams("baa","aa"))
print(findAnagrams("abacbabc","abc"))


