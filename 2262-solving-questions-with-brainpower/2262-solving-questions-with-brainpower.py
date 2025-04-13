class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
      self._questions = questions
      return self._dp(0)
    
    # base case - if idx >= len(questions) - return 0
    # for each we either take it's value + dp(idx + skip)
    # or take next value
    @cache
    def _dp(self, idx):
      if idx >= len(self._questions):
        return 0
      return max(self._questions[idx][0] + self._dp(idx + self._questions[idx][1] + 1), self._dp(idx + 1))
    