def moveZeroes(nums: list[int]):
    left = 0
    right = len(nums)-1

    while left<right:
        if(nums[left]==0):
            if nums[right]!=0:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            left += 1

    return nums

def moveZeroes2(nums: list[int]):
    left = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            if left<i:
                nums[left] = nums[left] + nums[i]
                nums[i] = nums[left] - nums[i]
                nums[left] = nums[left] - nums[i]
            left+=1


    return nums

print(moveZeroes2([0,12,0,0,1,0,6,0]))
