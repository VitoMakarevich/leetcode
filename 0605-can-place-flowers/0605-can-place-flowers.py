class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        self.local_zeros = 1
        def map_l(l):
          nonlocal n
          for v in l:
            if v:
              if self.local_zeros >= 3:
                n -= 1
                n -= max(0, int(floor((self.local_zeros - 3) / 2)))
              self.local_zeros = 0
            else:
              self.local_zeros += 1
            if n <= 0:
              return True
        return map_l(flowerbed) or map_l(deque([0, 1])) or False