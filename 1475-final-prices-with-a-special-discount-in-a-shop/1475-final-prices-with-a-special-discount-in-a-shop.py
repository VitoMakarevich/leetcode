class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final_prices = [0] * len(prices)
        q = deque()
        for idx in range(len(prices)):
          while q and prices[q[-1]] >= prices[idx]:
            item_with_discount = q.pop()
            final_prices[item_with_discount] = prices[item_with_discount] - prices[idx]
          q.append(idx)
        for idx in q:
          final_prices[idx] = prices[idx]

        return final_prices