def containsDuplicate(nums: [int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1
        return False
print(containsDuplicate([1,2,3,1]))