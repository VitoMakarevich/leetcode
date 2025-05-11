class Solution:
    # Comp complexity - O(N * K - unique numbers)
    # memory - O(N)
    def minOperations(self, nums: List[int]) -> int:
      zero_indexes = SortedList()
      elements = SortedDict()
      nums += [0]
      for index, value in enumerate(nums):
        if value == 0:
          zero_indexes.add(index)
        else:
          if not value in elements:
            elements[value] = []
          elements[value].append(index)
      op = 0
      for element, indexes in elements.items():
        idx = 0
        while idx < len(indexes):
          cur_position_in_nums = indexes[idx]
          first_zero_to_right_idx = zero_indexes.bisect_left(cur_position_in_nums)
          
          first_zero_to_right_idx = zero_indexes[first_zero_to_right_idx]
          last_index_to_pop = bisect_left(indexes, first_zero_to_right_idx) - 1
          for nullify_index in indexes[idx:last_index_to_pop + 1]:
            zero_indexes.add(nullify_index)
          idx = last_index_to_pop + 1
          op += 1
  
          
      return op