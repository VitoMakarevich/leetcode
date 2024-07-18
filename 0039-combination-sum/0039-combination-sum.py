class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sorted(candidates, reverse=True)
        print(candidates)
        self._rec(candidates, target, [], 0, res)
        return res

    def _rec(self, candidates, remain, itr, i, res):
      if remain == 0:
        print(f"appending {itr}")
        res.append(itr.copy())
        return
      
      if remain - candidates[i] >= 0:
        print(f"current, remain={remain}, itr={itr}, starting={candidates[i]}")
        itr.append(candidates[i])
        print(f"itr is {itr}")
        self._rec(candidates, remain - candidates[i], itr, i, res)
        itr.pop()
      else:
        print(f"skipping itr={itr}, remain={remain}, cur={candidates[i]}")
      if i < len(candidates) - 1:
        print(f"next, remain={remain}, itr={itr}, starting={candidates[i + 1]}")
        self._rec(candidates, remain, itr, i + 1, res)
      else:
        print(f"skipping next for cur i={i}, itr={itr}")
          

