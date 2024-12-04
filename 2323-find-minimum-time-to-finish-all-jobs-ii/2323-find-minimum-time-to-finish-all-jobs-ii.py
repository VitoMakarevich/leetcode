class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort(reverse = True)
        workers.sort(reverse = True)
        r = float('-inf')
        for i in range(len(jobs)):
          r = max(r, int(ceil(jobs[i] / workers[i])))
        return r