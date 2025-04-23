class Solution:
    def countLargestGroup(self, n: int) -> int:
      counter = defaultdict(int)
      for i in range(1, n + 1):
        number_sum = 0
        while i > 0:
          first_number = i % 10
          number_sum += first_number
          i -= first_number
          i //= 10
        counter[number_sum] += 1
      max_group_size = max(counter.values())
      return sum([int(value == max_group_size) for value in counter.values()])