class Solution:
    def longestPalindrome(self, s: str) -> str:
        current_longest = s[0]
        current_longest_length = 1
        result_holder = s[0]
        cache = [{j: True for j in range(len(s) - i) if j == 0} for i in range(len(s))]
        # print(cache)
        for i in range(len(s)):
            for j in reversed(range(i + 1, len(s))):
                if j - i >= current_longest_length:
                    # print(f"starting with i={i}, j={j}")
                    res = self._internal(s, cache, i, j)
                    if res:
                        length = j - i + 1
                        if current_longest_length < length:
                            current_longest = s[i: j+1]
                            current_longest_length = length
        return current_longest
    
    def _internal(self, s, cache, i, j):
        # print(f"i={i}, j={j}")
        if j - i not in cache[i]:
            if j == i + 1:
                cache[i][j - i] = s[i] == s[j]
            else:
                ends_match = s[i] == s[j]
                inside_match = self._internal(s, cache, i + 1, j - 1)
                cache[i][j - i] = ends_match and inside_match
        return cache[i][j - i]

        
        