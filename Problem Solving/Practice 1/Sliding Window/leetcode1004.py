def longestOnes(nums: [int], k: int) -> int:
    left = 0
    max_len = 0
    zero_counter = {1:0,0:0}
    for r in range(len(nums)):
        zero_counter[nums[r]] += 1
        while zero_counter[0] > k:
            zero_counter[nums[left]] -= 1
            left += 1
        curlen = r - left + 1
        if curlen > max_len:
            max_len = curlen
    return max_len
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))

