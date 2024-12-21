# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        options = words.copy()
        last_options = []
        
        while True:
          if len(last_options):
            options = list(filter(lambda x: self.accepted(x, last_options), options))
            popularity = self._calculate_dict_popularity(options)
            options.sort(key = lambda x: self._word_popularity(x, popularity), reverse=True)
          next_guess = options[0]
          options = options[1:]
         
          res = master.guess(next_guess)
          if res == 6:
            return
          last_options.append((res, next_guess))

    def _calculate_dict_popularity(self, candidates):
      res = []
      for i in range(6):
        local = {}
        for word in candidates:
          local[word[i]] = local.get(word[i], 0) + 1
        res.append(local)
      return res
    def _word_popularity(self, word, popularity_dict):
      r = 0
      for idx, c in enumerate(word):
        r += popularity_dict[idx][c]
      return r

    def accepted(self, candidate, prev):
      v = prev[-1]
      matches, word = v
      mismatches = 6 - matches
      
      positional_matches = self.position_match(candidate, word)
      positional_mismatches = 6 - positional_matches
      if positional_matches < matches or mismatches > positional_mismatches:
        return False
      return True

    def position_match(self, left, right):
      m = 0
      for i in range(len(left)):
        m += left[i] == right[i]
      return m