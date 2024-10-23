class Solution:
    def numSquares(self, n: int) -> int:
       cache = {}
       return self._dp(cache, n)

    def _dp(self, cache, n):
        if n == 0:
            return 0
        if not n in cache:
            max_sqrt = int(sqrt(n))
            possible_parts = [i * i for i in range(1, max_sqrt + 1)]
            cache[n] = 1 + min(map(
                lambda x: self._dp(cache, n - x),
                possible_parts
            ))
        return cache[n]

    