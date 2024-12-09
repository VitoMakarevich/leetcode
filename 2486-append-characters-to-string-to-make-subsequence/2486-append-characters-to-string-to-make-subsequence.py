class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        search_pointer = 0
        string_pointer = 0
        while string_pointer < len(s):
          if t[search_pointer] == s[string_pointer]:
            search_pointer += 1
          if search_pointer == len(t):
            return 0
          string_pointer += 1
        return len(t) - search_pointer