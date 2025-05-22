
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
      queries.sort(key = lambda x: x[0])

      heap = []
      ops = 0
      query_idx = 0
      delta = [0] * (len(nums) + 1)
      for idx, num in enumerate(nums):
        ops += delta[idx]  

        while query_idx < len(queries) and queries[query_idx][0] == idx:
          heappush(heap, -queries[query_idx][1])
          query_idx += 1
        while ops < num and heap and -heap[0] >= idx:
          ops += 1
          delta[-heappop(heap) + 1] -= 1
        if ops < num:
          return -1
      return len(heap)