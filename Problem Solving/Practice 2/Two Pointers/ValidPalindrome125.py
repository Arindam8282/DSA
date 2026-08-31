def validPalindrome(sentence:str) -> bool:
    trimmedWord = sentence.replace(' ','').replace(';','').replace(':','').replace(',','').lower()
    print(trimmedWord)
    lp = 0
    rp = len(trimmedWord) - 1
    while lp<rp:
        if trimmedWord[lp]!=trimmedWord[rp]:
            return False
        lp += 1
        rp -= 1
    return True
def validPalindrome2(sentence:str) -> bool:
    lp = 0
    rp = len(sentence) - 1
    while lp<rp:
        if not sentence[lp].isalnum():
            lp += 1
            continue
        if not sentence[rp].isalnum():
            rp -= 1
            continue
        if sentence[lp].lower()!=sentence[rp].lower():
            return False
        lp += 1
        rp -= 1
    return True
print(validPalindrome2("a man; a plan; a canal; panama"))
print(validPalindrome2("race, a , car"))
