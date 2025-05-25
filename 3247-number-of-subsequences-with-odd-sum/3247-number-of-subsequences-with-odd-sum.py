class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:
      mod = 10 ** 9 + 7
      even_count = 0
      odd_count = 0
      for n in nums:
        if n % 2 == 0:
          even_count += 1
        else:
          odd_count += 1

      even_subsets = pow(2, even_count, mod)

      if odd_count == 0:
          return 0
      odd_subsets = pow(2, odd_count - 1, mod)
      return (even_subsets * odd_subsets) % mod

    @cache
    def _comb(self, n, k):
      return factorial(n) // (factorial(k) * factorial(n - k))
    

