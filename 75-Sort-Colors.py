class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, i, high = 0,0, len(nums)-1
        while i <= high:
            if nums[i] < 1:
                nums[i], nums[low] = nums[low], nums[i]
                i += 1
                low += 1
            elif nums[i] > 1:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            else:
                i += 1
            