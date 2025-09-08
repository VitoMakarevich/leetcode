class Solution:
    def minOperations(self, s: str) -> int:
      smallest = inf
      max_chars = 26
      start_char = ord('a')
      for c in s:
        if c == 'a':
          pos = max_chars
        else:
          pos = ord(c) - start_char
        smallest = min(smallest, pos)
      return max_chars - smallest