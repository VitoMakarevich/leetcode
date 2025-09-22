class Spreadsheet:

    def _get_row_idx(self, coord):
      return ord(coord) - ord('A')

    def _coord_to_row_col(self, coord):
      row = self._get_row_idx(coord[:1])
      col = int(coord[1:]) 
      return row, col
     
    def __init__(self, rows: int):
      self.values = [{} for _ in range(26)]

    def setCell(self, cell: str, value: int) -> None:
      row, col = self._coord_to_row_col(cell)
      self.values[row][col] = value     

    def resetCell(self, cell: str) -> None:
      row, col = self._coord_to_row_col(cell)
      self.values[row][col] = 0


    def _is_coord(self, val):
      return not val[0].isdigit()
    def getValue(self, formula: str) -> int:
      formula = formula[1:]
      operands = formula.split('+')
      parts = []
      for v in operands:
        if self._is_coord(v):
          row, col = self._coord_to_row_col(v)
          parts.append(self.values[row].get(col, 0))
        else:
          parts.append(int(v))
      return sum(parts)

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)