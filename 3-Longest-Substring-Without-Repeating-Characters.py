class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length = 0
        chars = set()
        if not s:
            return max_length

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_length = max(max_length, len(chars))
            r += 1
        return max_length
            