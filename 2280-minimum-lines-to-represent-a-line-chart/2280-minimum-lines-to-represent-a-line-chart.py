class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
      if len(stockPrices) <= 2:
        return len(stockPrices) - 1
      stockPrices.sort()
      prev_point = stockPrices[1]
      prev_vector = self.get_a_b(stockPrices[0], stockPrices[1])
      res = 1
      for point in stockPrices[2:]:
        vector_with_cur = self.get_a_b(prev_point, point)
        if vector_with_cur != prev_vector:
          res += 1
          prev_vector = vector_with_cur
        prev_point = point
      return res
    
    def get_a_b(self, point1, point2):
      x1, y1 = point1
      x2, y2 = point2
      a = (y2 - y1) / (x2 - x1)
      b = y1 - a * x1
      return a, b