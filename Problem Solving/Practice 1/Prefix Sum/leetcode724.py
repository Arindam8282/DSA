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
print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))

        