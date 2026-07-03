def topKFrequent(nums: [int], k: int) -> [int]:
    seen = {}
    for num in nums:
        if num in seen:
            seen[num]+=1
        else:
            seen[num] = 1
    return sorted(seen,key = seen.get, reverse=True)[:k]
print(topKFrequent([1,1,1,2,2,3],2))
print(topKFrequent([1,2,1,2,1,2,3,1,3,2],2))
print(topKFrequent([1],1))

