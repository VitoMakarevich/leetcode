class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res = 0
        counter = defaultdict(int)
        for row in matrix:
          row_str = ''.join(str(x) for x in row)
          opp_row = ''.join(map(lambda x: str(1 - x), row))
          counter[row_str] += 1
          counter[opp_row] += 1
          res = max(res, counter[row_str], counter[opp_row])
        return res