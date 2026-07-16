class TimeMap:

    def __init__(self):
        self.time_store = defaultdict(list) # key : list of (timestamp, value)s

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.time_store[key]
        l, r = 0, len(values)-1
        while l <= r:
            m = l + (r-l) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m+1
            else:
                r = m-1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)