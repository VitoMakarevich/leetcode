import io

class Solution:

  def generateParenthesis(self, n: int) -> List[str]:
    to_open = n
    to_close = n
    res = []
    buf = []
    self._rec(buf, 2 * n, 0, n, res, False)
    return res
      
  def _rec(self, buf, target_l, left_open, allowed_to_open, res, last_left):
    if len(buf) == target_l:
      res.append(''.join(buf))
      return
    if not last_left:
      for i in range(1, allowed_to_open + 1):
        for o in range(i):
          buf.append('(')
        self._rec(buf, target_l, left_open + i, allowed_to_open - i, res, True)
        for o in range(i):
          buf.pop()
    if last_left:
      for i in range(1, left_open + 1):
        for o in range(i):
          buf.append(')')
        self._rec(buf, target_l, left_open - i, allowed_to_open, res, False)
        for o in range(i):
          buf.pop()