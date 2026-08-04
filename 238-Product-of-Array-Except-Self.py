class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        temp = 1
        for i in range(0, len(nums)-1):
            temp *= nums[i]
            res.append(temp)
        temp = 1
        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i+1]
            res[i] *= temp
        return res
