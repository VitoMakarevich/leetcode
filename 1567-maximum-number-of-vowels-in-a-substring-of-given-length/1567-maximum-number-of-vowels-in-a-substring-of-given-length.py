class Solution:
    _vowels = {'a', 'e', 'i', 'o', 'u'}
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k - 1

        vowels = self.count_vowels(s[0: k])
        res = vowels
        while right < len(s) - 1:
            is_left_vowel = s[left] in self._vowels
            is_new_vowel = s[right + 1] in self._vowels
            left = left + 1
            right = right + 1
            vowels -= int(is_left_vowel)
            vowels += int(is_new_vowel)
            res = max(vowels, res)
        
        return res
    
    def count_vowels(self, s):
        res = 0
        for c in s:
            if c in self._vowels:
                res += 1

        return res
        