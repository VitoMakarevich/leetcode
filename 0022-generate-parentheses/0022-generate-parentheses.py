import io

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        to_open = n
        to_close = n
        res = []
        buf = io.StringIO()
        self._rec("", 2 * n, 0, n, res, False)
        return res
        
    def _rec(self, buf, target_l, left_open, allowed_to_open, res, last_left):
      if len(buf) == target_l:
        res.append(buf)
        return
      if not last_left:
        for i in range(1, allowed_to_open + 1):
          for o in range(i):
            buf = buf + '('
          self._rec(buf, target_l, left_open + i, allowed_to_open - i, res, True)
          buf = buf[:-i]
      if last_left:
        for i in range(1, left_open + 1):
          for o in range(i):
            buf = buf + ')'
          self._rec(buf, target_l, left_open - i, allowed_to_open, res, False)
          buf = buf[:-i]
    
    def _remove_last_n_char(self, buffer, n):
      buf = io.StringIO()
      buf.write(buffer.getvalue()[:-n])
      return buf