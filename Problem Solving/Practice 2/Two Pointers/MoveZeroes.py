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
    write = 0
    
    for read in range(len(nums)):
        if nums[read] != 0:
            # Swap non-zero element to the write position
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
        print(write)
    return nums
moveZeroes([1,1,0,0,1,0,1])
moveZeroes2([0,0,1,0,1])
moveZeroes2([13,0,1,0,3,12])
moveZeroes2([1,0])

