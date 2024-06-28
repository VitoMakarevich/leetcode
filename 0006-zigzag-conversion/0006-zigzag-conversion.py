class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ["" for _ in range(numRows)]
        size = len(s)
        i = 0
        while i < size:
          row = 0
          while row < numRows and i < size:
            res[row] = res[row] + s[i]
            i += 1
            row += 1
          
          next_zag_row = numRows - 2
          while next_zag_row > 0 and i < size:
            res[next_zag_row] = res[next_zag_row] + s[i]
            i += 1
            next_zag_row -= 1


        return reduce(lambda a,b: a + b, res)
           