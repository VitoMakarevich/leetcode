class Solution:
    def sortVowels(self, s: str) -> str:
      s = list(s)
      vowels_set = set(['a', 'e', 'i', 'o', 'u'])
      vowels_in_str = []
      for c in s:
        if c.lower() in vowels_set:
          vowels_in_str.append(c)
      vowels_in_str.sort()
      ptr = 0
      for i, c in enumerate(s):
        if c.lower() in vowels_set:
          s[i] = vowels_in_str[ptr]
          ptr += 1
      return ''.join(s)