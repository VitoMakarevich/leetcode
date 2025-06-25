class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
      counter = Counter(word)
      letter_count = list(counter.items())

      letter_count.sort(key = lambda x: x[1])
      prefix_sum = [0]
      for item, count in letter_count:
        prefix_sum.append(prefix_sum[-1] + count)
      res = inf
      for index, (char, count) in enumerate(letter_count):
        local_res = prefix_sum[index]
        right_bigger = bisect_right(letter_count, count + k, key = lambda x: x[1])
        if right_bigger < len(letter_count):
          total_count_to_right = prefix_sum[-1] - prefix_sum[right_bigger]
          max_allowed_count = max(letter_count[right_bigger - 1][1], count + k)
          local_res += total_count_to_right - (len(letter_count) - right_bigger) * max_allowed_count
        res = min(local_res, res)
      return res
    # aabcaba
    # a - 4
    # b - 2
    # c - 1

    # dabdcbdcdcd
    # d - 5
    # a - 1
    # b - 2
    # c - 3

    #"ahahnhahhah"
    # a - 4
    # h - 6
    # n - 1
    
    # K = 1