def removeDuplicates(nums:[int]) -> [int]:
    slow = 0
    fast = 1
    while fast<len(nums):
        if(nums[fast]!=nums[slow]):
            slow += 1
            nums[slow] = nums[fast]    
        fast += 1
    return nums[:slow+1]
def removeDuplicates2(nums:[int]) -> [int]:
    return list(set(nums))



print(removeDuplicates2([1,1,2]))
print(removeDuplicates2([0,0,0,1,1,1,2,2,2,2,3,3,3,4]))
