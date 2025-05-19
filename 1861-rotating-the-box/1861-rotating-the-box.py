class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        res = [['.'] * len(boxGrid[0]) for _ in range(len(boxGrid))]
        for row in range(len(boxGrid)):
          last_stationary = len(boxGrid[0])
          stones = 1
          for column in range(len(boxGrid[0]) - 1, -1, -1):
            cur_item = boxGrid[row][column]
            if cur_item == '#':
              res[row][last_stationary - stones] = '#'
              stones += 1
            elif cur_item == '*':
              stones = 1
              last_stationary = column
              res[row][column] = '*'
          
        return list(zip(*res[::-1]))