class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_sequence = 0

        for num in nums:
            length = 0
            if num-1 not in nums:
                while num in nums:
                    length += 1
                    num += 1
            max_sequence = max(length, max_sequence)
        return max_sequence


