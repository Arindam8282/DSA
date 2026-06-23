def subarraySum(nums: [int], k: int) -> int:
    current_sum = 0
    count = 0
    dict1 = {0:1}
    for i in range(len(nums)):
        current_sum += nums[i]
        if (current_sum-k) in dict1:
            count+=dict1[current_sum-k]
        if current_sum in dict1:
            dict1[current_sum] += 1
        else:
            dict1[current_sum] = 1
    return count


print(subarraySum([1,1,1],3))