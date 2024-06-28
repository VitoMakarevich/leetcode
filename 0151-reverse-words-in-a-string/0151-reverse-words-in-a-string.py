from io import StringIO

class Solution:
    def reverseWords(self, s: str) -> str:
        res = StringIO()

        idx = len(s) - 1
        word_end = None
        while idx >= 0:
          if s[idx] == ' ':
            if word_end is not None:
              if len(res.getvalue()) > 0:
                res.write(" ")
              res.write(s[idx + 1:word_end + 1])
              word_end = None
          else:
            if word_end == None:
              word_end = idx
          idx -= 1
        
        # print(word_end)
        if word_end is not None:
          if len(res.getvalue()) > 0:
            res.write(" ")
          res.write(s[0:word_end + 1])
          word_end = None


        v = res.getvalue()
        res.close()
        return v