class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
      tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
      total = cur_energy = 0
      for to_finish, to_start in tasks:
        if to_start > cur_energy:
          diff = to_start - cur_energy
          total += diff
          cur_energy += diff
        cur_energy -= to_finish
      return total