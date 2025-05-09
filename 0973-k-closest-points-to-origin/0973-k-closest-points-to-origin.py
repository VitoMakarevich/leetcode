class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for p in points:
          dist = sqrt(p[0] ** 2 + p[1] ** 2)
          if len(q) < k:
            heapq.heappush(q, (-dist, p))
          elif len(q) == k and dist < -q[0][0]:
            heapq.heappushpop(q, (-dist, p))

        return list(map(lambda x: x[1], q))