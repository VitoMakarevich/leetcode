# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        options = words.copy()
        last_option = None
        
        while True:
          if last_option:
            lo_matches, lo_value = last_option
            options = list(filter(lambda x: self.position_match(lo_value, x) >= lo_matches, options))
          next_guess = options[0]
          options = options[1:]
          print(next_guess)
          res = master.guess(next_guess)
          if res == 6:
            return
          last_option = (res, next_guess)


    
    def position_match(self, left, right):
      m = 0
      for i in range(len(left)):
        m += left[i] == right[i]
      return m