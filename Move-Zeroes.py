class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        new_arr = [num for num in nums if num != 0]
        zero_arr = [0] * (len(nums)-len(new_arr))

        nums[:] = new_arr + zero_arr
        
        