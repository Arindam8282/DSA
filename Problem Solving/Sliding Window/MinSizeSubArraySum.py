def minSizeSubArraySum(nums:[int],target:int) -> int:
    lp = 0
    rp = -1
    windowsum = 0
    windowDict = {}
    while lp<len(nums):
        print(lp,rp,windowsum)
        if(windowsum==target):
            length = abs(rp-lp)
            if(target not in windowDict or windowDict[target]>length):
                windowDict[target] = length + 1
            if(rp<len(nums)-1):
                rp+=1
                windowsum += nums[rp]
            else:
                windowsum -= nums[lp]
                lp+=1
        elif(windowsum<target and rp<len(nums)-1):
            rp+=1
            windowsum += nums[rp]
        else:
            windowsum -= nums[lp]
            lp+=1
    return windowDict[target] if target in windowDict else 0

print(minSizeSubArraySum([1,1,1,1,1,1,1,1],11))
print(minSizeSubArraySum([1,4,4],4))
print(minSizeSubArraySum([2,3,1,2,4,3],7))


