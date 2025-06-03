class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
      available_boxes = set()
      visited = set()
      available_keys = set()
      q = deque()
      for init in initialBoxes:
        if status[init] == 1:
          q.append(init)
          visited.add(init)
        else:
          available_boxes.add(init)
      res = 0
      while q:
        cur = q.popleft()
        print(cur)
        res += candies[cur]
        for key in keys[cur]:
          status[key] = 1
          
        for box in containedBoxes[cur]:
          if not box in visited:
            available_boxes.add(box)
        
        for cand in available_boxes:
          if status[cand] == 1 and not cand in visited:
            visited.add(cand)
            q.append(cand)
  

      return res
        
      
      