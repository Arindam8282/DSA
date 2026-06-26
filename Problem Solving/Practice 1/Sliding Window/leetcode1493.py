def longestSubarray(nums: [int]) -> int:
    left = 0
    right = len(nums)-1
    leftSum = rightSum = 0
    
    while left!=right:
        if nums[left] and nums[right]:
            leftSum+=nums[left]
            rightSum+=nums[right]
            left+=1
            right-=1
        elif not nums[left] and not nums[left+1]:
            leftSum=0
            left+=2
        elif not nums[right] and not nums[right-1]:
            rightSum=0
            right-=2
        elif nums[left]:
            leftSum+=nums[left]
            left+=1
        elif nums[right]:
            rightSum+=nums[right]
            right-=1
        else:
            leftSum+=nums[left]
            rightSum+=nums[right]
            left+=1
            right-=1
        if left-1 > -1 and not nums[left-1]:
            leftSum = 0
        if right+1<len(nums) and not nums[right+1]:
            rightSum = 0
    return leftSum+rightSum
def longestSubarray2(nums:[int])->int:
    count_zero = 0
    max_length = 0
    left = right = 0
    for i in range(len(nums)):
        right+=1
        if nums[i] == 0:
            count_zero += 1
        while count_zero > 1:
            if nums[left] == 0:
                count_zero -= 1
            left += 1
        if max_length < right-left:
            max_length = right-left
    return max_length-1


print(longestSubarray2([1,1,0,1]))
print(longestSubarray2([0,1,1,1,0,1,1,0,1]))
print(longestSubarray2([1,1,1]))
print(longestSubarray2([1,1,0,0,1,1,1,0,1]))
print(longestSubarray2([1,0,0,0,0]))



        
        