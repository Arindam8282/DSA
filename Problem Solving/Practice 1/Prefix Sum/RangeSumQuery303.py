class NumArray:
    def __init__(self, nums: [int]):
        self.prefixList = [0]
        for i in range(len(nums)):
            self.prefixList.append(self.prefixList[i]+nums[i])
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixList[right+1]-self.prefixList[left]
        
# NumArray([-2, 0, 3, -5, 2, -1])
# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,5)
print(param_1)