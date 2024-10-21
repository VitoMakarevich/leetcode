class Solution:
    _vowels = {'a', 'e', 'i', 'o', 'u'}
    def maxVowels(self, s: str, k: int) -> int:
        right = k - 1

        vowels = self.count_vowels(s[0: k])
        res = vowels
        if res == k:
            return k
        while right < len(s) - 1:
            right = right + 1
            vowels -= int(s[right - k] in self._vowels)
            vowels += int(s[right] in self._vowels)
            res = max(vowels, res)
            if res == k:
                return k
        
        return res
    
    def count_vowels(self, s):
        res = 0
        for c in s:
            if c in self._vowels:
                res += 1

        return res
        