class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        self._word1 = word1
        self._word2 = word2
        self._cache = [{} for i in range(len(word1))]
        return self._minDistanceMemoryOptimized(len(word1) - 1, len(word2) - 1)

    def _minDistanceMemoryOptimized(self, i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if not j in self._cache[i]:
            if self._word1[i] == self._word2[j]:
                self._cache[i][j] = self._minDistanceMemoryOptimized(i - 1, j - 1)
            else:
                edit_distance = self._minDistanceMemoryOptimized(i - 1, j - 1)
                delete_distance = self._minDistanceMemoryOptimized(i - 1, j)
                add_distance = self._minDistanceMemoryOptimized(i, j - 1)
                self._cache[i][j] = 1 + min(edit_distance, delete_distance, add_distance)
        return self._cache[i][j]