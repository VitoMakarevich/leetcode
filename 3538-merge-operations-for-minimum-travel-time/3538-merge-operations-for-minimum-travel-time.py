class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # l - length of the road - same as `max(position)`
        # n - len(position)
        # k - max swaps
        # position - sign location
        # time[i] - speed per 1 km between position[i] and position[i + 1]
        @cache
        def _dp(k, position_idx, cur_speed):
          if position_idx == n - 1:
            if k == 0:
              return 0
            else:
              return inf
          if k > n - position_idx - 2:
            return inf
          # merge allowed next K intervals
          speed = cur_speed + time[position_idx]
          next_speed = 0
          res = inf
          for index in range(0, k + 1):
            cur_price = (position[position_idx + index + 1] - position[position_idx]) * speed
            if index > 0:
              next_speed += time[position_idx + index]
            local_res = _dp(k - index, position_idx + index + 1, next_speed)
            res = min(res, local_res + cur_price)
          return res
        return _dp(k, 0, 0)
