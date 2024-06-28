from collections import deque

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = deque()
        res = []
        self.add(n, k, stack, res)
        return res
        
    
    def add(self, options, k, stack, res):
      if len(stack) == k:
        res.append(list(stack))
      else:
        if stack:
            first_item = stack[-1]
        else:
            first_item = 0
        for i in range(first_item + 1, options + 1):
          # print(f"cur stack is {list(stack)}, running for i {i}")
          stack.append(i)
          self.add(options, k, stack, res)
          stack.pop()