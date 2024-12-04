class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        j_hq = []
        w_hq = []
        r = float('-inf')
        for v in jobs:
          heapq.heappush(j_hq, -v)
        for v in workers:
          heapq.heappush(w_hq, -v)
        while len(j_hq) > 0:
          r = max(r, int(ceil(heapq.heappop(j_hq) / heapq.heappop(w_hq))))
        return r