class MedianFinder:

    def __init__(self):
        self.smaller, self.larger = [], []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller, -num)
        if self.larger and -self.smaller[0] > self.larger[0]:
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))
        
        if len(self.smaller) > len(self.larger)+1:
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))
        if len(self.larger) > len(self.smaller)+1:
            heapq.heappush(self.smaller, -heapq.heappop(self.larger))

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -self.smaller[0]
        elif len(self.larger) > len(self.smaller):
            return self.larger[0]
        else:
            return float(-self.smaller[0]+self.larger[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()