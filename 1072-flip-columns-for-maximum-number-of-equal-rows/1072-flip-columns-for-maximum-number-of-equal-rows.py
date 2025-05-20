class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res = 0
        counter = defaultdict(int)
        for row in matrix:
          row_str = ''.join(str(x ^ row[0]) for x in row)
          counter[row_str] += 1
          
        return max(counter.values())