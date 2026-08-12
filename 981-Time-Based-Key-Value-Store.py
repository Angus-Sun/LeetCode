class TimeMap:
#hashmap of key : list of (timestamp, val)
    def __init__(self):
        self.key_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.key_map[key]
        if not values:
            return ""
        l, r = 0, len(values)-1
        largest = ""
        while l <= r:
            m = l + (r-l) // 2
            if values[m][0] <= timestamp:
                largest = values[m][1]
                l = m+1
            else:
                r = m-1
        return largest 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)