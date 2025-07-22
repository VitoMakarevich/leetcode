class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
      res = None
      for pos, v in enumerate(number):
        if v == digit:
          cand = int(number[:pos] + number[pos + 1:])
          if res == None:
            res = cand
          else:
            res = max(res, cand)
      return str(res)