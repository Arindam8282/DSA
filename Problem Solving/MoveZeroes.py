def moveZeroes(nums) -> None:
    l = -1
    r = 0
    if(0 in nums):
        i=0
        while i<len(nums):
            if(nums[i]==0):
                r += 1
            elif(nums[i]!=0):
                l += 1
                r = i
                if(l<r):
                    nums[l] = nums[l]+nums[r]
                    nums[r] = nums[l]-nums[r]
                    nums[l] = nums[l]-nums[r]
            i+=1
    print(nums)
        
def moveZeroes2(nums: list[int]) -> None:
    l = 0  
    for i in range(len(nums)):
        if nums[i] != 0:
            if l < i:
                nums[l] = nums[l] + nums[i]
                nums[i] = nums[l] - nums[i]
                nums[l] = nums[l] - nums[i]
            l += 1
    print(nums)
moveZeroes2([1,1,0,0,1,0,1])
moveZeroes2([0,0,1,0,1])
moveZeroes2([0,1,0,3,12])
moveZeroes2([1,0])

