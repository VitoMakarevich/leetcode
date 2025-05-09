class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        heapq.heapify(sticks)
        while len(sticks) != 1:
          first, second = heapq.heappop(sticks), heapq.heappop(sticks)
          new_size = first + second
          res += new_size
          heapq.heappush(sticks, new_size)
        return res
