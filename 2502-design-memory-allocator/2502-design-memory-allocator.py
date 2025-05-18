class Allocator:

    def __init__(self, n: int):
        self._memory = [0] * n
        self._mapping = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
      next_block_start = self._find_block_of_size(size)
      if next_block_start == -1:
        return -1
      self._mapping[mID].append((next_block_start, size))
      for idx in range(next_block_start, next_block_start + size):
        self._memory[idx] = mID
      return next_block_start

    def _find_block_of_size(self, size):
      idx = 0
      while idx < len(self._memory):
        
        while idx < len(self._memory) and self._memory[idx] != 0:
          idx += 1
        start_idx = idx
        block_size = 0
        while idx < len(self._memory) and self._memory[idx] == 0 and block_size < size:
          block_size += 1
          idx += 1
        if block_size == size:
          return start_idx
        idx += 1
      return -1
      

    def freeMemory(self, mID: int) -> int:
      blocks = self._mapping[mID]
      del self._mapping[mID]
      units = 0
      for (start, size) in blocks:
        units += size
        for idx in range(start, start + size):
          self._memory[idx] = 0
      return units


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)