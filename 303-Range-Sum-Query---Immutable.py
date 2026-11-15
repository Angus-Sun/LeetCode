class NumArray:

    def __init__(self, nums: list[int]):
            self.sumArr = [0] * (len(nums)+1)
            prefix = 0
            for i in range(len(nums)):
                prefix += nums[i]
                self.sumArr[i+1] = prefix
            
    def sumRange(self, left: int, right: int) -> int:
        left, right = left+1, right+1
        return self.sumArr[right]-self.sumArr[left-1]
#[0,1,2,3]
#[0,1,3,6]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)