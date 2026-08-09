class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        product = 1
        for i in range(len(nums)-1):
            product *= nums[i]
            res.append(product)
        # 1,2,3,4
        # 1, 1, 2, 6
        # 24  12  4 1
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            res[i] *= product
        return res
