class Solution:
    def makePalindrome(self, s: str) -> bool:
      center = len(s) // 2
      left = center if len(s) % 2 == 1 else center - 1
      right = center
      mismatch = 0
      while left >= 0 and right < len(s) and mismatch < 3:
        mismatch += s[left] != s[right]
        left -= 1
        right += 1
      return mismatch < 3