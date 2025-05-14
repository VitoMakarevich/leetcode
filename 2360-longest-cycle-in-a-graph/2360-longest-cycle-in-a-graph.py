class Solution:
    def longestCycle(self, edges: List[int]) -> int:
      res = -1
      
      visited = set()
      def dfs(start, cur_path, cur_idx):
        nonlocal res
        if start == -1:
            return
        if start in cur_path:
            res = max(res, cur_idx - cur_path[start])
            return
        if start in visited:
            return

        cur_path[start] = cur_idx
        dfs(edges[start], cur_path, cur_idx + 1)
        visited.add(start) 
      for idx in range(len(edges)):
        if not idx in visited:
          dfs(idx, {}, 0)
      return res
