class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
      primes_up_to_border = set(self.primes(int(sqrt(r))))
      range_size = r - l + 1
      special_count = 0
      for i in range(2, int(sqrt(r)) + 1):
          if i in primes_up_to_border:
              square = i * i
              if l <= square <= r:
                  special_count += 1
      return r - l + 1 - special_count
    
    def primes(self, right):
      is_available = [True] * (right + 1)
      for start in range(2, right + 1):
        if is_available[start]:
          for v in range(start ** 2, right + 1, start):
            is_available[v] = False
      return [idx for idx, av in enumerate(is_available[2:], start = 2) if av]