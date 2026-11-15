class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_nums = 0
        for num in num_set:
            if num-1 in num_set:
                continue
            count = 1
            next_num = num + 1
            while next_num in num_set:
                count += 1
                next_num += 1
            max_nums = max(max_nums, count)
        return max_nums
                
