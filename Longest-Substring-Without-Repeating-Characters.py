1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l, best = 0, 0
4        numSet = set()
5        for r in range(len(s)):
6            while s[r] in numSet:
7                numSet.remove(s[l])
8                l+= 1
9            numSet.add(s[r])
10            best = max(best, r-l+1)
11        return best