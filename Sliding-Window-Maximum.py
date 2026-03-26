1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        res = []
4        q = deque()
5        l = r = 0
6        while r < len(nums):
7            while q and nums[q[-1]] < nums[r]:
8                q.pop()
9            q.append(r)
10            
11            if q and l > q[0]:
12                q.popleft()
13            if r + 1 >= k:
14                res.append(nums[q[0]])
15                l += 1
16            r += 1
17        return res
18
19
20
21
22