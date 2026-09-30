class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_map = {}
        for index, val in enumerate(nums):
            diff = target - val
            if diff in index_map:
                return [index, index_map[diff]]
            index_map[val] = index