class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
      sign = ['-', ''][bool(numerator * denominator >= 0)]
      numerator, denominator = abs(numerator), abs(denominator)
      div, mod = divmod(numerator, denominator)
      res = str(div)
      if mod == 0:
        return sign + res
      res = res + '.'
      # pos of mod / denominator
      cache = {}
      mod *= 10
      idx = len(res)
      while mod > 0:
        if mod in cache:
          return sign + res[:cache[mod]] + '(' + res[cache[mod]:idx] + ')'
        cache[mod] = idx
        if mod < denominator:
          mod *= 10
          res += '0'
        else:
          div, mod = divmod(mod, denominator)
          mod *= 10
          res += str(div) 
        idx += 1
      return sign + res
