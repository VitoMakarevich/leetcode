class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
      if len(words) == 0:
        return words[0]
      search_val = groups[0]
      alt_val = int(not (bool(search_val)))

      search_val_pos = 0
      alt_pos = search_val_pos
      res = []
      while search_val_pos < len(groups):
        while alt_pos < len(groups) and groups[alt_pos] != alt_val:
          alt_pos += 1
        
        res.append(words[search_val_pos])
        if alt_pos < len(groups):
          res.append(words[alt_pos])

        search_val_pos = alt_pos + 1
        while search_val_pos < len(groups) and groups[search_val_pos] != search_val:
          search_val_pos += 1
        alt_pos = search_val_pos

        

      return res