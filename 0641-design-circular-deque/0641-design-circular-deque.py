class MyCircularDeque:

    def __init__(self, k: int):
        self._store = [0] * k
        self.maxSize = k
        self.head = None
        self.tail = None
        self.size = 0

    def isFull(self):
      if self.size == self.maxSize:
        return True
      else:
        return False

    def isEmpty(self):
      return self.size == 0
    def _init(self, value):
      self._store[0] = value
      self.head = 0
      self.tail = 0
      self.size = 1

    def _destroy(self):
      self.head = None
      self.tail = None
      self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
          return False
        elif self.head is None:
          self._init(value)
        else:
          new_pos = (self.maxSize + self.head - 1) % self.maxSize
          self._store[new_pos] = value
          self.size += 1
          self.head = new_pos
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
          return False 
        elif self.head is None:
          self._init(value)
        else:
          new_pos = (self.maxSize + self.tail + 1) % self.maxSize
          self._store[new_pos] = value
          self.size += 1
          self.tail = new_pos
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
          return False
        elif self.size == 1:
          self._destroy()
        else:
          new_pos = (self.maxSize + self.head + 1) % self.maxSize
          self.size -= 1
          self.head = new_pos
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
          return False
        elif self.size == 1:
          self._destroy()
        else:
          new_pos = (self.maxSize + self.tail - 1) % self.maxSize
          self.size -= 1
          self.tail = new_pos
        return True

    def getFront(self) -> int:
      if self.size == 0:
        return -1
      return self._store[self.head]

    def getRear(self) -> int:
      if self.size == 0:
        return -1
      return self._store[self.tail]




# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()