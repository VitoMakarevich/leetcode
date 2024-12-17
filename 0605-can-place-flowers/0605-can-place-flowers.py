class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        local_zeros = 1
        for v in flowerbed + [0, 1]:
          if v:
            if local_zeros >= 3:
              cnt += 1
              if local_zeros > 3:
                cnt += int(floor((local_zeros - 3) / 2))
            local_zeros = 0
          else:
            local_zeros += 1
          if cnt >= n:
            return True
        return False