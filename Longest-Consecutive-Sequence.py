1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        longestSequence = 0
4        numSet = set(nums)
5
6        for num in numSet:
7            if (num-1) not in numSet:
8                length = 1
9                while (num + length) in numSet:
10                    length += 1
11                longestSequence = max(length, longestSequence)
12        return longestSequence
13