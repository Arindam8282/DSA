
def validPalindrome(s: str) -> bool:
    lowerStr = ''.join(char for char in s if char.isalnum()).lower()
    print(lowerStr)
    left = 0
    right = len(lowerStr)-1
    flag = False
    while left<=right:
        if(lowerStr[left]!=lowerStr[right]):
            flag = True
            break
        else:
            left += 1
            right -= 1
    return not flag

def validPalindrome2(s: str) -> bool:
    left = 0
    right = len(s)-1
    while left<right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True

def validPalindrome3(s: str) -> bool:
    lowerStr = ''.join(char for char in s if char.isalnum()).lower()
    return lowerStr[::-1]==lowerStr 

    
print(validPalindrome3("race a e-car"))
# race a car