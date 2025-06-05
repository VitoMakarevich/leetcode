class Solution:
    
    def minOperations(self, n: int, m: int) -> int:
      n = str(n)
      m = str(m)
      self._primes = self.precompute_primes(int('9' * len(n)))
      if self.is_prime(n) or self.is_prime(m):
        return -1

      q = [(self.distance(n, m, int(n)), int(n), n)]
      visited = set()
      while q:
         
        dist, cur_sum, cur_num = heapq.heappop(q)

        if cur_num == m:
          return cur_sum
        if cur_num in visited:
          continue
        visited.add(cur_num)
        for neighbour in self.neighbors(cur_num):
          if not neighbour in visited:
            heapq.heappush(q, (
                self.distance(neighbour, m, cur_sum),
                cur_sum + int(neighbour),
                neighbour,
              )
            )
      return -1

    def distance(self, n, m, prev):
        return sum(a != b for a, b in zip(n, m)) + prev

    def precompute_primes(self, top):
      primes = [True] * (top + 1)
      primes[0] = False
      primes[1] = False
      for base in range(2, top + 1):
        if primes[base]:
          for square in range(base * base, top + 1, base):
            primes[square] = False
      return primes
    
    def neighbors(self, cur):
      res = []
      for idx, val in enumerate(cur):
        val = int(val)
        if val < 9:
          cand = cur[:idx] + str(val + 1) + cur[idx + 1:]
          if not self.is_prime(int(cand)):
            res.append(cand)
        if val > 0:
          cand = cur[:idx] + str(val - 1) + cur[idx + 1:]
          if not self.is_prime(int(cand)) and not (idx == 0 and val == 1):
            res.append(cand)
      return res

    def is_prime(self, n):
      return self._primes[int(n)]