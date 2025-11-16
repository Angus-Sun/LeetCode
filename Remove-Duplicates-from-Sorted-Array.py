class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_map = {} # val : 1
        count = 0
        new_nums = []
        n = len(nums)
        for i in range(n):
            if num_map.get(nums[i], False) == False:
                num_map[nums[i]] = True
                count += 1
                new_nums.append(nums[i])
        nums[:] = new_nums
        return count
