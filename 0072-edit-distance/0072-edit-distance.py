class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        return self._minDistanceMemoryOptimized(word1, word2, len(word1) - 1, len(word2) - 1)

    @lru_cache(None)
    def _minDistanceMemoryOptimized(self, word1, word2, i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if word1[i] == word2[j]:
            return self._minDistanceMemoryOptimized(word1, word2, i - 1, j - 1)
        else:
            edit_distance = self._minDistanceMemoryOptimized(word1, word2, i - 1, j - 1)
            delete_distance = self._minDistanceMemoryOptimized(word1, word2, i - 1, j)
            add_distance = self._minDistanceMemoryOptimized(word1, word2, i, j - 1)
            return 1 + min(edit_distance, delete_distance, add_distance)