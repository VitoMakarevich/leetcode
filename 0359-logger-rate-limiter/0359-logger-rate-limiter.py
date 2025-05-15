class Logger:

    def __init__(self):
        self._storage = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if not message in self._storage or abs(self._storage[message] - timestamp) >= 10:
            self._storage[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)