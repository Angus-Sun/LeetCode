class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {} # num : count
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)
        
        for num, count in count_map.items():
            freq[count].append(num)
        
        result = []
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        

        
            
