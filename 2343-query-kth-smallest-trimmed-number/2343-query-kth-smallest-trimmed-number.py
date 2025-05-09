class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        q_with_index = [(index, query)  for index, query in enumerate(queries)]
        num_with_index = [(idx, v) for idx, v in enumerate(nums)]

        trim_to_query = defaultdict(list)
        min_trim_level = -inf
        max_trim_level = len(nums[0])
        
        for index, (position, trim_size) in q_with_index:
          trim_to_query[trim_size].append((index, position - 1))
          min_trim_level = max(min_trim_level, trim_size)
        
        res = [0] * len(queries)
        for trim_level in range(max_trim_level - 1, max_trim_level - min_trim_level - 1, -1):
          num_with_index = self._bucket_sort(num_with_index, trim_level)
          kth_trimmed = max_trim_level - trim_level
          for answer_index, position in trim_to_query[kth_trimmed]:
            out = num_with_index[position][0]
            res[answer_index] = out

        return res
    
    def _bucket_sort(self, nums, pos):
      buckets = [0] * 10
      for n in nums:
        buckets[int(n[1][pos])] += 1
      cumulative_count = [0]
      for idx in range(len(buckets) - 1):
        cumulative_count.append(cumulative_count[-1] + buckets[idx])
      new_list = [0] * len(nums)
      for n in nums:
        bucket = cumulative_count[int(n[1][pos])]
        new_list[bucket] = n
        cumulative_count[int(n[1][pos])] += 1
      return new_list