class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      res = []
      candidates.sort()
      def backtrack(cur_sum, cur_idx, cur_list):
        nonlocal res
        if cur_sum == target:
          res.append(list(cur_list))
          return
        if cur_sum > target:
          return
        for i in range(cur_idx, len(candidates)):
          if i > cur_idx and candidates[i] == candidates[i - 1]:
            continue
          cur_sum += candidates[i]
          cur_list.append(candidates[i])
          backtrack(cur_sum, i + 1, cur_list)
          cur_sum -= candidates[i]
          cur_list.pop()
      
      backtrack(0, 0, [])
      return res
