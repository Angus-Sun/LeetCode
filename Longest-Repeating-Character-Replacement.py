1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        count = {}
4        maxF = 0
5        res = 0
6        l = 0
7        for r in range(len(s)):
8            count[s[r]] = 1 + count.get(s[r], 0)
9            maxF = max(maxF, count[s[r]])
10            while (r-l+1) - maxF > k:
11                count[s[l]] -= 1
12                l += 1
13            res = max(res, r-l+1)
14        return res