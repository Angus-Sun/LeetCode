class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:
            minheap.append((x**2+y**2, x, y))
        heapq.heapify(minheap)
        res = []
        while k > 0:
            value = heapq.heappop(minheap)
            res.append([value[1], value[2]])
            k -= 1
        return res
