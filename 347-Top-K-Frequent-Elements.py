class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            num_map[num] = 1 + num_map.get(num, 0)
        
        freq = [[] for i in range(len(nums)+1)]
        for num in num_map:
            freq[num_map[num]].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
