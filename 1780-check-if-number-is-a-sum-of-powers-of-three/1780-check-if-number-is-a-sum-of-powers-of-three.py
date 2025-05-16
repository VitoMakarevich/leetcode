class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        max_pow = ceil(log(10 ** 7, 3))
        powers_of_3 = [3 ** n for n in range(max_pow + 1)]
        
        prev_pow = max_pow + 1
        while n > 0:
          bigger_or_equal_power = bisect_left(powers_of_3, n)
          if powers_of_3[bigger_or_equal_power] > n:
            bigger_or_equal_power -= 1
          if bigger_or_equal_power == prev_pow:
            return False
          n -= powers_of_3[bigger_or_equal_power]
          prev_pow = bigger_or_equal_power
        return n == 0