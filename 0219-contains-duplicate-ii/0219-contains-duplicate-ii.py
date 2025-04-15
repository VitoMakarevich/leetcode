class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      storage = defaultdict(list)
      for index, value in enumerate(nums):
        storage[value].append(index)
      for indexes in storage.values():
        if len(indexes) > 1:
          prev = indexes[0]
          for next_index in indexes[1:]:
            if next_index - prev <= k:
              return True
            prev = next_index
      return False