class Solution:
    def sortVowels(self, s: str) -> str:
      s = list(s)
      vowels_lower = ['a', 'e', 'i', 'o', 'u']
      vowels_set = set(vowels_lower + [c.upper() for c in vowels_lower])
      vowels_in_str = []
      for c in s:
        if c in vowels_set:
          vowels_in_str.append(c)
      vowels_in_str.sort(reverse = True)
      for i, c in enumerate(s):
        if c in vowels_set:
          s[i] = vowels_in_str[-1]
          vowels_in_str.pop()
      return ''.join(s)