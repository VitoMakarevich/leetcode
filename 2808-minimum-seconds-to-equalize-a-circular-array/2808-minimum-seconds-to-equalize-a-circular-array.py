class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
      store = defaultdict(list)
      size = len(nums)
      for idx, v in enumerate(nums):
        store[v].append(idx)
      res = (size) // 2
      for _, indexes in store.items():
        time = (size - indexes[-1] + indexes[0]) // 2
        for f, s in zip(indexes, indexes[1:]):
          time = max(time, (s - f) // 2)
        res = min(res, time)
      return res
      