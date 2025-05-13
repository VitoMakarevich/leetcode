class Solution:
    def numDistinct(self, s: str, t: str) -> int:
      @cache
      def dp(i, j):
        if j == len(t):
          return 1
        if i == len(s):
          return 0
        candidates = []
        if_skip_in_left = dp(i + 1, j)
        cur_char_equal = s[i] == t[j]
        if_current_equals = dp(i + 1, j + 1) if cur_char_equal else 0
        return if_current_equals + if_skip_in_left

      return dp(0, 0)
