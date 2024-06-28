import heapq
class Node:

  def __init__(self, val, distance, turn):
    self._val = val
    self._distance = distance
    self._turn = turn

  
  def __lt__(self, other):
    return self._distance < other._distance
    
  @staticmethod
  def new_instance(val, target, turn):
    diff = 0
    for i in range(len(target)):
      if val[i] != target[i]:
        diff += 1

    return Node(val, diff + turn, turn)

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        checked_set = set()
        pq = []
        variants = set()
        for i in wordList:
          variants.add(i)
        for opt in self._get_options(variants, beginWord):
          heapq.heappush(pq, Node.new_instance(opt, endWord, 2))
          checked_set.add(opt)
        while len(pq) > 0:
          nxt = heapq.heappop(pq)
          checked_set.add(nxt._val)
          if nxt._val == endWord:
            return nxt._turn
          for opt in self._get_options(variants, nxt._val):
            if opt not in checked_set:
              heapq.heappush(pq, Node.new_instance(opt, endWord, nxt._turn + 1))
        
        return 0



        
    def _get_options(self, opts, cur):
      res = []
      for i in range(len(cur)):
        for letter in range(ord('a'), ord('z')+1):
          if chr(letter) != cur[i]:
            cand = StringIO()
            if i != 0:
              cand.write(cur[:i])
            cand.write(chr(letter))
            if i != len(cur) - 1:
              cand.write(cur[i+1:])
            val = cand.getvalue()
            if val in opts:
              res.append(val)
      return res
        