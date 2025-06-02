class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
      free = SortedSet()
      res = list(rains)
      state = {}
      for idx, day in enumerate(rains):
        if day in state:
          free_slot = free.bisect_right(state[day])
          if free_slot == len(free):
            return []
          else:
            free_day = free[free_slot]
            res[free_day] = day
            free.discard(free_day)
            res[idx] = -1
            state[day] = idx
        elif day != 0:
          res[idx] = -1
          state[day] = idx
        else:
          free.add(idx)
      while free:
        min_item = free[0]
        free.discard(min_item)
        res[min_item] = 1
      return res