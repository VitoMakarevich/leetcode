class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = deque()
        ans = [0] * len(temperatures)
        for idx in range(len(temperatures)):
          while q and temperatures[q[-1]] < temperatures[idx]:
            prev_idx = q.pop()
            day_to_higher_temp = idx - prev_idx
            ans[prev_idx] = day_to_higher_temp
          q.append((idx))
        return ans
          