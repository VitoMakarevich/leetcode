class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._heap = []
        self._k = k
        for v in nums:
            if len(self._heap) < k:
                heapq.heappush(self._heap, v)
            else:
                if v > self._heap[0]:
                    heapq.heappushpop(self._heap, v)
                    

    def add(self, val: int) -> int:
        if len(self._heap) < self._k or self._heap[0] < val:
          heapq.heappush(self._heap, val)
          if len(self._heap) > self._k:
            heapq.heappop(self._heap)
        return self._heap[0]

          


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)