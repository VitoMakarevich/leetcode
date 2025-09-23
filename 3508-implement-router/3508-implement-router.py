class Router:

    def __init__(self, memoryLimit: int):
      self.packets = set()
      self.queue = deque()
      self.max_size = memoryLimit
      self.packets_by_destination = defaultdict(list)
      self.last_discarded_package = None

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
      package = (source, destination, timestamp)
      if package in self.packets:
        return False
      self.packets.add(package)
      self.queue.append(package)
      self.packets_by_destination[destination].append(package)
      if len(self.queue) > self.max_size:
        self.forwardPacket()
      return True

    def forwardPacket(self) -> List[int]:
      if len(self.queue):
        pkg = self.queue.popleft()
        self.last_discarded_package = pkg
        self.packets.discard(pkg)
        self.packets_by_destination[pkg[1]].pop(0)
        return list(pkg)
      return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
      packages_by_destination = self.packets_by_destination[destination]
      left = bisect.bisect_left(packages_by_destination, startTime, key = lambda x:x[2])
      right = bisect.bisect_right(packages_by_destination, endTime, key = lambda x:x[2])

      return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)