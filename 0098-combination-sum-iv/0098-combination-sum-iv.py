class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = [0 for i in range(target + 1)]
        nums.sort()
        filtered = list(filter(lambda x: x <= target, nums))
        cache[0] = 1
        for i in range(1, target + 1):
            for n in filtered:
                if i - n >= 0:
                    cache[i] += cache[i - n]

        return cache[target]
