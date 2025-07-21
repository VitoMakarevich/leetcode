class Solution:
    def longestValidParentheses(self, s: str) -> int:
      store = defaultdict(list)
      counter = 0
      for idx, v in enumerate(s):
        if v == '(':
          counter += 1
        else:
          counter -= 1
        store[counter].append(idx)
      res = 0
      for counter_value, indexes in store.items():
        res = max(res, indexes[-1] - indexes[0])
      return res