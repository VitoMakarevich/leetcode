class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        current_number_count = 1
        max_zeros = len(str(k))
        cache = [0] * (len(s) + 1)
        cache[0] = 1
        for i in range(len(s)):
          if s[i] == '0':
            continue
          for v in range(min(
            len(s) - i,
            max_zeros
          )):
            cur_value = s[i: i + v + 1]
            if int(cur_value) <= k:
              cache[i + v + 1] += cache[i]
        MOD = 10**9 + 7
        return cache[len(s)]% MOD
