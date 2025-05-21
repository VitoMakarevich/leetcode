class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
      s = SortedDict()
      for n in nums:
        if not n in s:
          s[n] = 0
        s[n] += 1
      
      counts = SortedDict()
      for item, count in s.items():
        if not count in counts:
          counts[count] = set()
        counts[count].add(item)

      while len(counts) > 1 or (len(counts) == 1 and len(counts.peekitem(0)[1])) > 1:
        most_popular_values_count, most_popular_values  = counts.peekitem(-1)
        mid = next(iter(most_popular_values))
       
        if len(most_popular_values) > 1:
          next_item = next(islice(most_popular_values, 1, 2))
          most_popular_values.discard(next_item)
          if most_popular_values_count > 1:
            if not most_popular_values_count - 1 in counts:
              counts[most_popular_values_count - 1] = set()
            counts[most_popular_values_count - 1].add(next_item)
        else:
          next_popular_count, next_popular_values = counts.peekitem(-2)
          next_item = next(iter(next_popular_values))
          next_popular_values.discard(next_item)
          if next_popular_count > 1:
            if not next_popular_count - 1 in counts:
              counts[next_popular_count - 1] = set()
            counts[next_popular_count - 1].add(next_item)
          if len(next_popular_values) == 0:
            del counts[next_popular_count]
        
        most_popular_values.discard(mid)
        if most_popular_values_count > 1:
          if not most_popular_values_count - 1 in counts:
            counts[most_popular_values_count - 1] = set()
          counts[most_popular_values_count - 1].add(mid)
        if len(most_popular_values) == 0:
            del counts[most_popular_values_count]
        print(counts)
        
        
      return sum(counts.keys())