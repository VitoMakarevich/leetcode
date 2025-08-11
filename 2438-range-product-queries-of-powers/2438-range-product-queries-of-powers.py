class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
      mod = 10 ** 9 + 7
      cur_pow = 0
      cur_v = 2 ** cur_pow
      
      while n >= cur_v:
        cur_pow += 1
        cur_v *= 2
      
      cur_v //= 2

      remain = n
      res = []
      while remain > 0:
        if remain >= cur_v:
          res.append(cur_v)
          remain -= cur_v
        else:
          cur_v //= 2
      res.reverse()
      
      prefix_prod = [1]
      for v in res:
        prefix_prod.append((prefix_prod[-1] * v) % mod)
      
      output = []

      def mod_inv(x):
          return pow(x, mod - 2, mod)

      for start, end in queries:
          numerator = prefix_prod[end + 1]
          denominator = prefix_prod[start]
          prod = numerator * mod_inv(denominator) % mod
          output.append(prod)
      return output
