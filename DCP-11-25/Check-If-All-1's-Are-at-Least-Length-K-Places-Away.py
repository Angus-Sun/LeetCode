class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        first1 = True
        for num in nums:
            if num == 1:
                if count < k and first1 == False:
                    return False
                else:
                    count = 0
                    first1 = False
            else:
                count += 1
        return True
