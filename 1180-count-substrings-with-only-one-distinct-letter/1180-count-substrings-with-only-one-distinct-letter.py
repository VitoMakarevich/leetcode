class Solution:
    def countLetters(self, s: str) -> int:
        s += '-'
        repeat_count = 0
        idx = 1
        prev = s[0]
        prev_count = 1
        res = 0
        while idx < len(s):
          if s[idx] == prev:
            prev_count += 1
          else:
            res += prev_count * (prev_count + 1) // 2
            prev = s[idx]
            prev_count = 1
          idx += 1
        return res