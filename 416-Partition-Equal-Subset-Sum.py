class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums)-1,-1,-1):
            new_dp = set()
            for t in dp:
                if nums[i]+t == target:
                    return True
                new_dp.add(t)
                new_dp.add(t+nums[i])
            dp = new_dp 
        return False