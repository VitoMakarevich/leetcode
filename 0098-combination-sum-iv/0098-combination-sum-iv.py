class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.cache = {0: 1}
        self.filtered = sorted(nums)

        return self.count(target)

    def count(self, n):
        if n in self.cache:
            return self.cache[n]
        if n < 0:
            return 0
        if n == 0:
            return 1
        
        cnt = 0
        for cur in self.filtered:
            if n - cur < 0:
                break
            cnt += self.count(n - cur)
        
        self.cache[n] = cnt
        return cnt

        