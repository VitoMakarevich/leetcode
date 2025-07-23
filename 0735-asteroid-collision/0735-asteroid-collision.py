class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
      q = deque()
      for ast in asteroids:
        if not q or ast >= 0 or (q[-1] < 0 and ast < 0):
          q.append(ast)
        else:
          while q:
            if q[-1] > 0 and q[-1] == -ast:
              q.pop()
              break
            elif q[-1] > 0 and q[-1] > -ast:
              break
            else:
              q.pop()
              if not q or q[-1] < 0:
                q.append(ast)
                break
          


          
          
      return list(q)
