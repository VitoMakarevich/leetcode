class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        struct = {}
        for employee, head in enumerate(manager):
          if not employee == headID:
            ex = struct.get(head, [])
            ex.append(employee)
            struct[head] = ex
        self.struct = struct
        self.head_id = headID
        self.manager = manager
        self.inform_time = informTime
        return self._dfs(headID)

    def _dfs(self, emp):
      cur = 0
      sub = self.struct.get(emp, [])
      if len(sub):
        cur = self.inform_time[emp]
        return cur + max([self._dfs(s) for s in sub])
      return 0