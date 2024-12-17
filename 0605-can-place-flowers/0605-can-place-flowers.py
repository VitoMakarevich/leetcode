class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        self.cnt = 0
        self.local_zeros = 1
        def map_l(l):
          for v in l:
            if v:
              if self.local_zeros >= 3:
                self.cnt += 1
                self.cnt += max(0, int(floor((self.local_zeros - 3) / 2)))
              self.local_zeros = 0
            else:
              self.local_zeros += 1
            if self.cnt >= n:
              return True
        return map_l(flowerbed) or map_l(deque([0, 1])) or False