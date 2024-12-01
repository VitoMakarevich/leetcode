class Solution:
    def minSwaps(self, data: List[int]) -> int:
      total_count_ones = sum(data)
      count_ones = 0
      count_zeros = 0
      res = float('inf')
      for i, v in enumerate(data):
        if count_ones + count_zeros < total_count_ones:
          if v == 1:
            count_ones += 1
          else:
            count_zeros += 1
        else:
          
          total_cnt = count_ones + count_zeros
          l = i - total_cnt 
          res = min(res, count_zeros)
          if data[l] == 0:
            count_zeros -= 1
          else:
            count_ones -= 1
          if v == 1:
            count_ones += 1
          else:
            count_zeros += 1
          res = min(res, count_zeros)

        # print(f"i={i}, count_zeros={count_zeros}, count_ones={count_ones}, res={res}")

      return res