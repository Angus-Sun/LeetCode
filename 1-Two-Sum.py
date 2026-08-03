class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} # val : index

        for index, val in enumerate(nums):
            diff = target - val
            if diff in num_map:
                return [num_map[diff], index]
            num_map[val] = index