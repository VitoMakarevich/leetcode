class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
      combs = set()
      left = 0
      for right in range(len(s)):
        if right - left + 1 == k:
          combs.add(s[left:right + 1])
          left += 1
      return len(combs) == 2 ** k