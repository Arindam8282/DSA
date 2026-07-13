from collections import Counter
def minWindow(s: str, t: str) -> str:
    need_map = Counter(t)
    lp = rp = 0
    coords = []
    min_len = float('inf')
    window_map = {}
    def is_valid():
        for char in need_map:
            if window_map.get(char, 0) < need_map[char]:
                return False
        return True
    while rp<len(s):
        window_map[s[rp]] = window_map.get(s[rp],0)+1
        while is_valid():
            dis = rp - lp + 1
            if dis<min_len:
                min_len = dis
                coords = [lp,rp]
            left_char = s[lp]
            window_map[left_char] -= 1
            lp += 1
        rp+=1
        
    return s[coords[0]:coords[1]+1] if coords else ""
print(minWindow("ADOBECODEBLANC","ABC"))
print(minWindow("a","aa"))

