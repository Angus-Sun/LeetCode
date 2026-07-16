class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i+1, len(nums)-1
            while j < k:
                threeSum = val + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([val, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
        return res