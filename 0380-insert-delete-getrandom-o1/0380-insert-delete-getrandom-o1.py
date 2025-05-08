class RandomizedSet:

    def __init__(self):
        self._s = {}
        self._elements = []

    def insert(self, val: int) -> bool:
        if val in self._s:
          return False
        self._elements.append(val)
        pos = len(self._elements) - 1
        self._s[val] = pos
        return True

    def remove(self, val: int) -> bool:
        if not val in self._s:
          return False
        to_delete_pos = self._s[val]
        prev_last = self._elements[-1]
        self._elements[-1], self._elements[to_delete_pos] = self._elements[to_delete_pos], self._elements[-1]
        self._s[prev_last] = to_delete_pos
        self._elements.pop()
        del self._s[val]
        return True

    def getRandom(self) -> int:
        return self._elements[random.randint(0, len(self._elements) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()