class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #okay so my first thought is to use something like a hashmap to store the count of each element
        # we could then use liek a freq array basically put the values in buckets for the counts
        # we know the max a number can occur is the length of nums itself so thats the length of the freq array
        # we can then just do a for loop iterating backwards and pop from the bucket with most elements to get res until k is 0 
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        freq = [[] for i in range(len(nums)+1)]
        for key, val in count_map.items():
            freq[val].append(key)

        res = []

        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                k -= 1
                res.append(num)
                if k == 0:
                    return res
            