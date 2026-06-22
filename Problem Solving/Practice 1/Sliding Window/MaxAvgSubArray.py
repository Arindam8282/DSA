def findMaxAverage(nums: [int], k: int) -> float:
        windowsum = sum(nums[:k])
        maxsum = windowsum
        
        for i in range(k,len(nums)):
            windowsum = windowsum + nums[i] - nums[i-k]
            if(windowsum>maxsum):
                maxsum = windowsum
        return maxsum / k

print(findMaxAverage([-1],1))