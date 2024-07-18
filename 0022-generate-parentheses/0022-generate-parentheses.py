import io

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        buf = io.StringIO()
        self._rec(buf, 2 * n, 0, n, res, False)
        return res
        
    def _rec(self, buf, target_l, left_open, allowed_to_open, res, last_left):
        if len(buf.getvalue()) == target_l:
            res.append(buf.getvalue())
            return
        if not last_left:
            for i in range(1, allowed_to_open + 1):
                for o in range(i):
                    buf.write('(')
                self._rec(buf, target_l, left_open + i, allowed_to_open - i, res, True)
                buf.seek(len(buf.getvalue()) - i)  # Backtrack by seeking to the previous position
                buf.truncate()
        if last_left:
            for i in range(1, left_open + 1):
                for o in range(i):
                    buf.write(')')
                self._rec(buf, target_l, left_open - i, allowed_to_open, res, False)
                buf.seek(len(buf.getvalue()) - i)  # Backtrack by seeking to the previous position
                buf.truncate()