class Solution:
    def longestPalindrome(self, s: str) -> str:
        current_longest = s[0]
        current_longest_length = 1
        result_holder = s[0]
        cache = [[None if i != j else True for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                res = self._internal(s, cache, i, j)
                if res:
                    length = j - i + 1
                    if current_longest_length < length:
                        current_longest = s[i: j+1]
                        current_longest_length = length
        
        return current_longest
    
    def _internal(self, s, cache, i, j):
        if cache[i][j] is None:
            if j == i + 1:
                cache[i][j] = s[i] == s[j]
            else:
                ends_match = s[i] == s[j]
                inside_match = self._internal(s, cache, i + 1, j - 1)
                cache[i][j] = ends_match and inside_match
        return cache[i][j]

        
        