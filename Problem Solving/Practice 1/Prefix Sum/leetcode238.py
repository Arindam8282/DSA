def productExceptSelf(nums: [int]) -> [int]:
    totalPro = 1
    for i in nums:
        totalPro*=i
    leftPro = 1
    outlist = []
    for i in range(len(nums)):
        rightPro = (totalPro // leftPro) // nums[i]
        outlist.append(leftPro*rightPro)
        leftPro *= nums[i]
    return outlist
print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
