class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        s_mapping = defaultdict(list)
        for idx, char in enumerate(list(s)):
          s_mapping[char].append(idx)
        res = 0
        for word in words:
          current_s_idx = -1
          
          t_position = -1
          w_found = True
          for c in word:
            
            pos = self._bisect_right(s_mapping[c], t_position)
            if pos == len(s_mapping[c]):
                w_found = False
                break
            t_position = s_mapping[c][pos]
              
          res += int(w_found)
        return res

    def _bisect_right(self, values, target):
      low, high = 0, len(values)
      while low < high:
        mid = (low + high) // 2
        if values[mid] > target:
          high = mid
        else:
          low = mid + 1
      return low