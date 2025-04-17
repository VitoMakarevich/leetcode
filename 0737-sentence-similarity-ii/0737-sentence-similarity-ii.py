class UF:
  def __init__(self, size):
    self._parent = [i for i in range(size)]
    self._size = [1] * size

  def find(self, x):
    if x != self._parent[x]:
      self._parent[x] = self.find(self._parent[x])
    return self._parent[x]
  
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    if self._size[root_x] < self._size[root_y]:
      root_x, root_y = root_y, root_x
    self._parent[root_y] = root_x
    self._size[root_x] += self._size[root_y]

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
          return False
        word_index = 0
        words = {}
        for w1, w2 in similarPairs:
          if w1 not in words:
            words[w1] = word_index
            word_index += 1
          if w2 not in words:
            words[w2] = word_index
            word_index += 1
        uf = UF(word_index)
        for w1, w2 in similarPairs:
          uf.union(words[w1], words[w2])
        for w1, w2 in zip(sentence1, sentence2):
          if w1 != w2 and (w1 not in words or w2 not in words or uf.find(words[w1]) != uf.find(words[w2])):
            return False
        return True
