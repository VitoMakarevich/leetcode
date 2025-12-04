def _util(value, price, search):
  if len(value) == 0:
    return 0, value
  new_str = [value[0]]
  res = 0
  for d in value[1:]:

    comb = new_str[-1] + d
    if comb == search:
      new_str.pop()
      new_str.append('S')
      res += price
    elif not (new_str[-1] == 'S' and d == 'S'):
      new_str.append(d) 
  return res, ''.join(new_str)

class Solution:
    def countCollisions(self, directions: str) -> int:
      res = 0
      new = directions
      for price, pattern in [(2, 'RL'), (1, 'SL')]:
        prev = new
        collisions, new = _util(new, price, pattern)
        res += collisions
      res += _util(new[::-1], 1, 'SR')[0]
      return res

      

      