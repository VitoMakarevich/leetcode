class Solution:
    @lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        edit_distance = self.minDistance(word1[:-1], word2[:-1])
        delete_distance = self.minDistance(word1[:-1], word2)
        add_distance = self.minDistance(word1, word2[:-1])

        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])
        else:
            return 1 + min(edit_distance, delete_distance, add_distance)