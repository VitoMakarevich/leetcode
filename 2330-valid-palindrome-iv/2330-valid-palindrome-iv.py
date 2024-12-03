class Solution:
    def makePalindrome(self, s: str) -> bool:
      if len(s) == 1:
        return True
      center = len(s) // 2
      left = center if len(s) % 2 == 1 else center - 1
      right = center
      mismatch = 0
      while left >= 0 and right < len(s) and mismatch < 3:
        mismatch += s[left] != s[right]
        # print(f"l = {left}, r = {right}, mismatch = {mismatch}")
        left -= 1
        right += 1
      # print(mismatch)
      return mismatch < 3