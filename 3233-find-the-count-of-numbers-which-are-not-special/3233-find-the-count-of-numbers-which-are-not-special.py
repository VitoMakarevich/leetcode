class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
      primes_up_to_border = set(self.primes(int(sqrt(r))))
      range_size = r - l + 1
      special_count = 0
      for prime in primes_up_to_border:
        special_count += int(l <= prime * prime <= r)

      return r - l + 1 - special_count
    
    def primes(self, right):
      is_available = [True] * (right + 1)
      for start in range(2, right + 1):
        if is_available[start]:
          for v in range(start ** 2, right + 1, start):
            is_available[v] = False
      return [idx for idx, av in enumerate(is_available[2:], start = 2) if av]