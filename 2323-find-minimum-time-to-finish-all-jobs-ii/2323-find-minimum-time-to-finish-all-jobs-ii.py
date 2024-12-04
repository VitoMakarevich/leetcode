class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort(reverse = True)
        workers.sort(reverse = True)
        r = float('-inf')
        for i in range(len(jobs)):
          local_r = 0
          if jobs[i] <= workers[i]:
            local_r = 1
          else:
            local_r = ceil(jobs[i] / workers[i])
          r = max(r, local_r)
        return r