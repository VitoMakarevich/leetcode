class UF:
  def __init__(self):
    self._data = {}

  def find_root(self, a):
    root = self._data[a]
    res = 0
    if root != a:
      self._data[a] = root
      res = self.find_root(root)
    else:
      res = root
    return res
  
  def union(self, existing, new):
    existing_root = self.find_root(existing)
    new_root = self.find_root(new)
    self._data[new] = existing_root

  def add(self, new):
    self._data[new] = new

  def exists(self, new):
    return new in self._data

  def longest(self):
    res = {}
    for item in self._data:
      root = self.find_root(item)
      if not root in res:
        res[root] = 1
      else:
        res[root] += 1
    
    return max(res.values()) if len(res) > 0 else 0
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # uf = UF()
        # for n in nums:
        #   uf.add(n)
        
        # for n in nums:
        #   if uf.exists(n - 1):
        #     uf.union(n - 1, n)
        #   if uf.exists(n + 1):
        #     uf.union(n + 1, n)
        # return uf.longest()
        s = set(nums)

        m = 0
        for n in s:
          if n - 1 in s:
            continue
          else:
            l = 1
            nxt = n + 1
            while nxt in s:
              l += 1
              nxt = nxt + 1
            m = max(m, l)

        return m

        


    