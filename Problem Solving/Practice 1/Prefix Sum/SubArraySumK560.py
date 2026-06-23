def subarraySum(nums: [int], k: int) -> int:
    current_sum = 0
    prefixList = [0]
    count = 0
    dict1 = {0:1}
    for i in range(len(nums)):
        current_sum = prefixList[i] + nums[i]
        prefixList.append(current_sum)
        if (current_sum-k) not in dict1:
            dict1[current_sum] = 1
        else:
            dict1[current_sum] += 1
            count+=1
    return count


print(subarraySum([1,1,1],1))