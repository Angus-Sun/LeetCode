class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob(nums):
            rob1, rob2 = 0,0
            #[rob1, rob2, n, n+1, ...]
            for num in nums:
                temp = max(num+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(rob(nums[1:len(nums)]), rob(nums[:len(nums)-1]))