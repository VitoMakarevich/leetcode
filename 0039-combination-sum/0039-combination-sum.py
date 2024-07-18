class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self._rec(candidates, target, [], 0, res)
        return res

    def _rec(self, candidates, remain, itr, i, res):
      if remain == 0:
        res.append(itr.copy())
        return
      
      if remain - candidates[i] >= 0:
        itr.append(candidates[i])
        self._rec(candidates, remain - candidates[i], itr, i, res)
        itr.pop()
      if i < len(candidates) - 1:
        self._rec(candidates, remain, itr, i + 1, res)
