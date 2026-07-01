def twoSum(nums: [int], target: int) -> [int]:
    seen = {}
    for i in range(len(nums)):
        current = target - nums[i]
        if current in seen:
            return [seen[current],i]
        seen[nums[i]] = i

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
