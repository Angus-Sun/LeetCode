1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0, len(nums)-1
4        while l < r:
5            mid = l + (r-l)//2
6            if nums[mid] < nums[r]:
7                r = mid
8            else:
9                l = mid + 1
10        return nums[l]