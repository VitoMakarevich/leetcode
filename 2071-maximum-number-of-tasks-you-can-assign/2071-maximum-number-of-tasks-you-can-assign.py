class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        workers.sort()
        tasks.sort()
        m, n = len(tasks), len(workers)
        def is_possible_to_complete(task_count):
          pill_count = pills
          complete_count = 0
          workers_sorted = SortedList(workers[-task_count:])
          for task in tasks[:task_count][::-1]:
            if workers_sorted[-1] >= task:
              workers_sorted.pop()
              complete_count += 1
            else:
              if pill_count == 0:
                return False
              weakest_worker_within_range = workers_sorted.bisect_left(task - strength)
              if weakest_worker_within_range == len(workers_sorted):
                return False
              pill_count -= 1
              workers_sorted.pop(weakest_worker_within_range)

          return True
          


        low, high = 0, min(m, n)
        ans = 0
        while low <= high:
          mid = (low + high) // 2
          res = is_possible_to_complete(mid)
          if not res:
            high = mid - 1
          else:
            ans = mid
            low = mid + 1
        return ans