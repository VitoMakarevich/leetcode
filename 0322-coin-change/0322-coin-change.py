from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        return self.find_next(cache, amount, coins, 0)

    def find_next(self, cache, amount, coins, turn):
        if amount == 0:
          return 0
        if amount in cache:
          return cache[amount]
        candidates = deque()
        for coin in coins:
          if amount - coin >= 0:
            val_for_remain = self.find_next(cache, amount - coin, coins, turn)
            if val_for_remain != -1:
              candidates.append(val_for_remain)
        if len(candidates) == 0:
          cache[amount] = -1
          return -1
        res = min(candidates) + 1
        cache[amount] = res
        return res