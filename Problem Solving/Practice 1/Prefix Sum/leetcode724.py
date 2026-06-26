def pivotIndex(nums: [int]) -> int:
    leftSum = 0
    pivot = 0
    rightSum = 0
    rpivot = len(nums)-1
    leftSum+=nums[pivot]
    rightSum+=nums[rpivot]
    while pivot<rpivot:
        if leftSum==rightSum and pivot+1!=rpivot:
            return pivot+1
        elif rightSum==0:
            return pivot
        if leftSum<rightSum:
            pivot+=1
            leftSum+=nums[pivot]
        else:
            rpivot-=1 
            rightSum+=nums[rpivot]
    return -1
def pivotIndex2(nums:[int])-> int:
    leftSum = 0
    totalSum = sum(nums)
    for i in range(len(nums)):
        rightSum = totalSum - leftSum - nums[i]
        if leftSum == rightSum:
            return i
        leftSum+=nums[i]
    return -1

print(pivotIndex2([1,7,3,6,5,6]))
print(pivotIndex2([1,2,3]))
print(pivotIndex2([2,1,-1]))

        