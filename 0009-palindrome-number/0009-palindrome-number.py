class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
          return False
        numbers = []
        while x > 0:
          numbers.append(x % 10)
          x -= x % 10
          x //= 10
        l = 0
        r = len(numbers) - 1
        while l < r:
          if numbers[l] != numbers[r]:
            return False
          l += 1
          r -= 1
        return True
