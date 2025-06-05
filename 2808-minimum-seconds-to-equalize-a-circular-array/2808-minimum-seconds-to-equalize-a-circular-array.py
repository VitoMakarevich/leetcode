class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
      store = defaultdict(list)
      size = len(nums)
      for idx, v in enumerate(nums):
        store[v].append(idx)
      res = ceil((size - 1) / 2)
      for _, indexes in store.items():
        time = ceil((size - 1 - indexes[-1] + indexes[0]) / 2)
        for f, s in zip(indexes, indexes[1:]):
          time = max(time, ceil((s - 1 - f) / 2))
        res = min(res, time)
      return res