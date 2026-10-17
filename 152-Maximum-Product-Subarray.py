class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxNum = 1
        minNum = 1
        res = nums[0]
        for num in nums:
            temp = num * maxNum
            maxNum = max(num*maxNum, num, num*minNum)
            minNum = min(num*minNum, num, temp)
            res = max(maxNum, res)
        return res