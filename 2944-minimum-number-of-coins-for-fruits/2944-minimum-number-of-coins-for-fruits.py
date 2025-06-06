class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        cache = {}
        res = self._dp(cache, 0, prices)
        print(cache)
        return res
    
    def _dp(self, cache, pos, prices):
        if pos >= len(prices):
            return 0
        if pos not in cache:
            # print(f"for pos {pos} max_allowed_gap_to_skip is {max_allowed_gap_to_skip}, min_required_to_buy={min_required_to_buy}, range_adjustment={range_adjustment}")
            r = range(1, pos + 3)

            res = prices[pos] + min(
                self._dp(cache, pos + i, prices) for i in r
            )
            cache[pos] = res
            return res
        return cache[pos]