class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        cache = {}
        max_step = max(map(lambda x: len(x), wordDict))
        res = self._dp(s, 0, cache, wordset, max_step)
        return res

    def _dp(self, s, index, cache, words, max_step):
        if index > len(s) - 1:
            return True
        if index in cache:
            return cache[index]
        if not index in cache:
            for i in range(1, max_step + 1):
                candidate = s[index:index + i + 1]
    
                if candidate in words:
                    if self._dp(s, index + i + 1, cache, words, max_step):
                        cache[index] = True
                        return True
            cache[index] = False
        return False

        
            
