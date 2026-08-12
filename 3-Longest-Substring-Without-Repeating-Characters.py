class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, l, r =0, 0, 0
        
        char_set = set()
        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest = max(longest, r-l+1)
            r += 1
        return longest

