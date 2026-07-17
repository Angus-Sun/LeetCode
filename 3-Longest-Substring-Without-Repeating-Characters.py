class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, best = 0, 0
        numSet = set()
        for r in range(len(s)):
            while s[r] in numSet:
                numSet.remove(s[l])
                l+= 1
            numSet.add(s[r])
            best = max(best, r-l+1)
        return best