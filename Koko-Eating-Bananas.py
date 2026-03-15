1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        l, r = 1, max(piles)
4        speed = r
5        while (l <= r):
6            hours = 0
7            mid = l + (r-l)//2
8            for pile in piles:
9                hours += pile//mid
10                if pile % mid > 0:
11                    hours += 1
12            if hours <= h:
13                speed = mid
14                r = mid-1
15            else:
16                l = mid + 1
17        return speed