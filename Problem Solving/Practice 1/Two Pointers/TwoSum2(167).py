def twoSum(nums: [int],target: int) -> [int]:
    l = 0
    r = len(nums)-1
    out = []
    while l<r:
        sum = nums[l]+nums[r]
        if(sum>target):
            r -= 1
        elif(sum==target):
            out = [l,r]
            break
        else:
            l += 1
    return out
print(twoSum([2,7,14,22],9))