class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
          return self.multiply(num2, num1)

        temp_sum = []
        for char2 in num2[::-1]:
          temp_char = 0
          overflow, remainder = 0, 0
          power = 0
          for char1 in num1[::-1]:
            int2, int1 = int(char2), int(char1)
            position_value = int2 * int1 + overflow
            overflow, remainder = divmod(position_value, 10)
            temp_char += remainder * 10 ** power
            power += 1
          temp_char += overflow * 10 ** power
          temp_char *= 10 ** len(temp_sum)
          temp_sum.append(temp_char)
        return str(sum(temp_sum))