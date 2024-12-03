class Solution:
    def makePalindrome(self, s: str) -> bool:
      l = len(s)
      center = len(s) // 2
      left = center if l % 2 == 1 else center - 1
      right = center
      mismatch = 0
      while left >= 0 and right < l and mismatch < 3:
        mismatch += s[left] != s[right]
        left -= 1
        right += 1
      return mismatch < 3