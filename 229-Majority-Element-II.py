class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if len(count) <= 2:
                continue
            new_count = {}
            for num in count:
                if count[num] > 1:
                    new_count[num] = count[num] - 1
            count = new_count
        res  = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res