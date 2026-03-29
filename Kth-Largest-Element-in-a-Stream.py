1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.k = k
5        self.nums = nums
6        heapq.heapify(nums)
7        while len(self.nums) > self.k:
8            heapq.heappop(self.nums)    
9
10    def add(self, val: int) -> int:
11        heapq.heappush(self.nums, val)
12        if len(self.nums) > self.k:
13            heapq.heappop(self.nums)
14        return self.nums[0]
15
16
17# Your KthLargest object will be instantiated and called as such:
18# obj = KthLargest(k, nums)
19# param_1 = obj.add(val)