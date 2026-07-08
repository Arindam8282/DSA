def checkInclusion(s1: str, s2: str) -> bool:
    if s1 in s2 or s1[::-1] in s2:
        return True
    elif(s1.replace(s1[0],'')==''):
        return False
    for ch in s1:
        altchars = s1.replace(ch,'')
        for i in range(len(altchars)):
            perm = altchars.replace(altchars[i],ch+altchars[i])
            if perm in s2:
                return True
        if altchars+ch in s2:
            return True
    return False

def checkInclusion2(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
        
    s1_count = Counter(s1)
    window_count = Counter(s2[:len(s1)]) # Initialize the first window
    
    if s1_count == window_count:
        return True
        
    # Now, slide the window across s2
    for i in range(len(s1), len(s2)):
        # 1. Add the incoming character on the right
        incoming_char = s2[i]
        window_count[incoming_char] += 1
        
        # 2. Remove the outgoing character on the left
        outgoing_char = s2[i - len(s1)]
        window_count[outgoing_char] -= 1
        if window_count[outgoing_char] == 0:
            del window_count[outgoing_char] # Clean up to match keys perfectly
            
        # 3. Check if maps match
        if window_count == s1_count:
            return True
            
    return False

print(checkInclusion("abc","aidbacooo"))
print(checkInclusion("abc","bbbca"))
print(checkInclusion("ccc","cbac"))

