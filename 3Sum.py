1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res = []
5        for i, a in enumerate(nums):
6            if i > 0 and nums[i] == nums[i-1]:
7                continue
8            l, r = i+1, len(nums)-1
9            while (l < r):
10                threeSum = a + nums[l] + nums[r]
11                if threeSum > 0:
12                    r -= 1
13                elif threeSum < 0:
14                    l += 1
15                else:
16                    res.append([a, nums[l], nums[r]])
17                    l += 1
18                    while (nums[l-1] == nums[l] and l < r):
19                        l += 1
20        return res