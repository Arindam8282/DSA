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
def minSizeSubArraySum2(nums:[int],target:int)->int:
    lp = 0
    windowsum = 0
    min_length = float('inf')
    for rp in range(len(nums)):
        windowsum+=nums[rp]
        while windowsum>=target:
            winlength = rp-lp+1
            if(winlength<min_length):
                min_length = winlength
            windowsum -= nums[lp]
            lp+=1
    return min_length


print(minSizeSubArraySum([1,1,1,1,1,1,1,1],11))
print(minSizeSubArraySum([1,4,4],4))
print(minSizeSubArraySum2([2,3,1,2,4,3],7))
print(minSizeSubArraySum2([5,1,3,5,10,7,4,9,2,8],15))
print(minSizeSubArraySum2([1,2,3,4,5],11))




