class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        columns = len(mat[0])
        r = []
        for index, row in enumerate(mat):
            power = self._soilder_count(row, columns)
            
            if len(r) < k:
              heapq.heappush(r, (-power, -index))
            elif -r[0][0] > power:
              heapq.heappop(r)
              heapq.heappush(r, (-power, -index))
        
        res = []
        while r:
          res.append(-heapq.heappop(r)[1])
        return res[::-1]
        
    def _soilder_count(self, row, columns):
      low = 0
      high = columns
      while low < high:
        mid = (low + high) // 2
        if row[mid] == 0:
          high = mid
        else:
          low = mid + 1

      return low
