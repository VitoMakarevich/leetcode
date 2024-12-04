class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        j_s = sorted(jobs, reverse=True)
        w_s = sorted(workers, reverse = True)
        r = float('-inf')
        for i in range(len(jobs)):
          r = max(r, int(ceil(j_s[i] / w_s[i])))
        return r