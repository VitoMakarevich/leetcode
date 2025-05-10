class StockSpanner:

    def __init__(self):
        self._q = deque()
        self._day = 0

    def next(self, price: int) -> int:
        consequtive_days = 1
        while self._q and self._q[-1][1] <= price:
          consequtive_days += self._q.pop()[0]
        self._q.append((consequtive_days, price))
        return consequtive_days
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)