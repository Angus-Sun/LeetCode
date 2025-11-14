class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {} #val : index
        for index, key in enumerate(nums):
            diff = target - key
            if diff in sums:
                return [sums[diff], index]
            sums[key] = index 
        return


