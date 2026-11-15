class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #store some sort of prefix and postfix product
        #2 passes one for the prefix one for the postfix
        res = [1]*len(nums)
        num = 1
        for i in range(1, len(nums)):
            num *= nums[i-1]
            res[i] = num
        num = 1
        for i in range(len(nums)-2,-1,-1):
            num *= nums[i+1]
            res[i] *= num 
        return res