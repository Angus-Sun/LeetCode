1class Solution:
2    def trap(self, height: List[int]) -> int:
3        if not height:
4            return 0
5        l, r = 0, len(height)-1
6        maxL, maxR = height[l], height[r]
7        res = 0
8        while l < r:
9            if height[l] < height[r]:
10                l+= 1
11                maxL = max(maxL, height[l])
12                res += maxL-height[l]
13            else:
14                r -= 1
15                maxR = max(maxR, height[r])
16                res += maxR - height[r]
17        return res