import heapq

class TaskNode:
  def __init__(self, turn, target, val):
    self.distance = 0
    self.turn = turn
    self.value = val
    for i, v in enumerate(target):
      if val[i] != v:
        self.distance += 1
    
    self.distance += turn

  def __lt__(self, other):
    # Compare tasks based on their priority
    return self.distance < other.distance


class Solution:
    options = ["A", "G", "C", "T"] 

    def _all_options(self, startGene, genes):
      res = []
      
      for i in range(len(startGene)):
        for opt in self.options:
          if opt != startGene[i]:
            candidate = startGene[:i] + opt + startGene[i + 1:]
            if candidate in genes:
              res.append(candidate)

      return res

    def _is_solvable(self, start, end, bank):
      for pos in range(len(start)):
        if start[pos] == end[pos]:
          continue
        is_solvable = False
        for b in bank:
            is_solvable = is_solvable or b[pos] == end[pos]
        if not is_solvable:
          return False
      return True

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if not self._is_solvable(startGene, endGene, bank):
          return -1
        bank_set = set(bank)
        queue = []
        turn = 0
        visited = set()

        heapq.heappush(queue, TaskNode(0, endGene, startGene))
        visited.add(startGene)
        while len(queue) > 0:
          nxt = heapq.heappop(queue)
          visited.add(nxt.value)
          if nxt.value == endGene:
            return nxt.turn
          for cand in self._all_options(nxt.value, bank_set):
            if cand not in visited:
              heapq.heappush(queue, TaskNode(nxt.turn + 1, endGene, cand))
        
        return -1

