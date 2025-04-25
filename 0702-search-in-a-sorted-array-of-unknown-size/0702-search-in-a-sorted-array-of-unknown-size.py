# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    VALUE_MISSING = 2 ** 32 - 1
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low, high = 0, 10 ** 4
        
        while low < high:
          mid = (low + high) // 2
          mid_element = reader.get(mid)
          if Solution.VALUE_MISSING == mid_element:
            high = mid
            continue
          if mid_element >= target:
            high = mid
          else:
            low = mid + 1
        return low if reader.get(low) == target else -1