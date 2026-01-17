1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        max_area = 0
4        l, r = 0, len(height)-1
5        while l < r:
6            max_height = min(height[l], height[r])
7            max_area = max(max_area, max_height * (r - l))
8            if height[r] > height[l]:
9                l += 1
10            else:
11                r -= 1
12        return max_area
13