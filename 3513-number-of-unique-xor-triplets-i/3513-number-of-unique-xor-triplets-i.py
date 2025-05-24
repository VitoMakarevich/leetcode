class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        uniq = set()
        for i in range(len(nums)):
          for j in range(i, len(nums)):
            for k in range(j, len(nums)):
              uniq.add(nums[i] ^ nums[j] ^ nums[k])
        return len(uniq)