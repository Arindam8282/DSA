def productExceptSelf(nums: [int]) -> [int]:
    outlist = [1]*len(nums)
    totalPro = 1
    for i in range(len(nums)):
        outlist[i] = totalPro
        totalPro*=nums[i]
    leftPro = 1
    for i in range(len(nums)-1,-1,-1):
        outlist[i] *= leftPro
        leftPro *= nums[i]
    return outlist
print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
