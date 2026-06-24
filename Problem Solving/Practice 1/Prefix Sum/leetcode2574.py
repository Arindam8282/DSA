
def leftRightDifference(nums: [int]) -> [int]:
    totalsum = sum(nums)
    lsum = 0
    outlist = []
    for i in nums:
        rightsum = totalsum - lsum - i
        outlist.append(abs(lsum-rightsum))
        lsum+=i
    return outlist

print(leftRightDifference([0]))