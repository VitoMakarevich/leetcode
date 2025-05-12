class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values_with_key = self.storage[key]
        idx = bisect_right(values_with_key, timestamp, key = lambda x: x[0])
        if len(values_with_key) == 0 or (idx == 0 and timestamp < values_with_key[idx][0]):
          return ""
        return values_with_key[idx - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)