1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        res, i = [], 1
4        for j in range(len(nums)):
5            res.append(i)
6            i *= nums[j]
7        i = 1
8        for j in range(len(nums)-1, -1, -1):
9            res[j] *= i
10            i *= nums[j]
11        return res