1from collections import deque
2class RecentCounter:
3
4    def __init__(self):
5        self.counter = deque()
6
7    def ping(self, t: int) -> int:
8        self.counter.append(t)
9        while self.counter and self.counter[0] < t-3000:
10            self.counter.popleft()
11        return len(self.counter)
12
13
14# Your RecentCounter object will be instantiated and called as such:
15# obj = RecentCounter()
16# param_1 = obj.ping(t)