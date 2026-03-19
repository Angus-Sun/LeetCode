1class TimeMap:
2
3    def __init__(self):
4        self.store = defaultdict(list)
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        self.store[key].append([value, timestamp])
8
9    def get(self, key: str, timestamp: int) -> str:
10        res = ""
11        values = self.store[key]
12        l, r = 0, len(values)-1
13        while l <= r:
14            mid = l+(r-l)//2
15            if timestamp >= values[mid][1]:
16                res = values[mid][0]
17                l = mid + 1
18            else:
19                r = mid - 1
20        return res
21
22
23# Your TimeMap object will be instantiated and called as such:
24# obj = TimeMap()
25# obj.set(key,value,timestamp)
26# param_2 = obj.get(key,timestamp)