class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        all_negative = all(map(lambda x: x <= 0, arr))
        size = len(arr)
        if all_negative:
          return 0
        arr_sum = sum(arr)
        max_sum_to_left = [(arr[0], 0)] * (2 * len(arr))
        if k == 1:
          cur_sum = arr[0]
          max_sum = cur_sum
          for v in arr[1:]:
            cur_sum = max(cur_sum + v, v)
            max_sum = max(max_sum, cur_sum)
          return max_sum % mod

        for idx in range(1, 2 * len(arr)):
          real_idx = idx % size
          prev_sum, prev_sum_start = max_sum_to_left[idx - 1]
          sum_if_add = (prev_sum, prev_sum_start + 1) if prev_sum_start + size == idx else (prev_sum + arr[real_idx], prev_sum_start)
          sum_if_cur = (arr[real_idx], idx)
          if sum_if_cur[0] >= sum_if_add[0]:
            max_sum_to_left[idx] = sum_if_cur
          else:
            max_sum_to_left[idx] = sum_if_add
        
        max_sum_to_right = [(arr[-1], 2 * size - 1)] * (2 * len(arr))
        for idx in range(2 * len(arr) - 2, -1, -1):
          real_idx = idx % size
          prev_sum, prev_sum_start = max_sum_to_right[idx + 1]
          sum_if_add = (prev_sum, prev_sum_start - 1) if prev_sum_start - size == idx else (prev_sum + arr[real_idx], prev_sum_start)
          sum_if_cur = (arr[real_idx], idx)
          if sum_if_cur[0] >= sum_if_add[0]:
            max_sum_to_right[idx] = sum_if_cur
          else:
            max_sum_to_right[idx] = sum_if_add
        
        max_sum = -inf
        arr_sum = max(arr_sum, 0)
        for idx, ((left_sum, left_start), (right_sum, right_start)) in enumerate(zip(max_sum_to_left, max_sum_to_right)):
          if idx < size:
            max_sum = max(max_sum, left_sum + arr_sum * (k - 1), right_sum + arr_sum * (k - 2))
          else:
            max_sum = max(max_sum, left_sum + arr_sum * (k - 2), right_sum + arr_sum * (k - 1))
        return max_sum % mod
        