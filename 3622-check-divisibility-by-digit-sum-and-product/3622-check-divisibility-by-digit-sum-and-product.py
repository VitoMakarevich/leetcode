class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nums = []
        copy_n = n
        while copy_n > 0:
          div, mod = divmod(copy_n, 10)
          nums.append(mod)
          copy_n = div
        s = sum(nums)
        pr = prod(nums)
        return n % (s + pr) == 0