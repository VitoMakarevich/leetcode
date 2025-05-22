class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
      profit_capital = [(profit, capital) for profit, capital in zip(profits, capital)]
      profit_capital.sort(key = lambda x: x[1])
      current_money = w
      profit_capital_idx = 0
      heap = []
      for i in range(k):
        while profit_capital_idx < len(profit_capital) and profit_capital[profit_capital_idx][1] <= current_money:
          heappush(heap, -profit_capital[profit_capital_idx][0])
          profit_capital_idx += 1
        if heap:
          current_money += -heappop(heap)
      return current_money
