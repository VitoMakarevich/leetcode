class Solution:
    def primePalindrome(self, n: int) -> int:
      max_num_length = min(9, (len(str(n)) + 3))
      max_num = int('9' * max_num_length)
      
      primes = self.get_primes(max_num)

      for cand in primes:
        if cand >= n and self.is_palindrome(cand):
          return cand

    def get_primes(self, top):
      candidates = [True] * (top + 1)
      candidates[0] = False
      candidates[1] = False
      for base in range(2, top + 1):
        if candidates[base]:
          for val in range(base * base, top + 1, base):
            candidates[val] = False
      return [idx for idx, v in enumerate(candidates) if v]
    
    def is_palindrome(self, candidate):
      str_val = str(candidate)
      i = 0
      j = len(str_val) - 1
      
      while i <= j:
        if str_val[i] != str_val[j]:
          return False
        i += 1
        j -= 1
      return True

      