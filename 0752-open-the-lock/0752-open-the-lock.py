class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
          return -1
        visited = set(self._str_to_tuple(v) for v in deadends)
        queue = deque([self._str_to_tuple('0000')])
        move = 0
        target_tuple = self._str_to_tuple(target)
        visited.add(self._str_to_tuple('0000'))

        while queue:
          for _ in range(len(queue)):
            cur = queue.popleft()
            if cur == target_tuple:
              return move
            for adj in self._get_adj(cur):
              if not adj in visited:
                queue.append(adj)
                visited.add(adj)
          move += 1
        return -1

    def _str_to_tuple(self, val):
      return tuple(int(v) for v in val)

    def _get_adj(self, val):
      v_list = list(val)
      res = []
      for i in range(len(val)):
        res.append(tuple(v_list[:i] + [(val[i] + 1) % 10] + v_list[i + 1:]))
        res.append(tuple(v_list[:i] + [val[i] - 1 if val[i] > 0 else 9] + v_list[i + 1:]))
      return res