class Trie:

    def __init__(self):
        self._head = TrieNode(None)
        

    def insert(self, word: str) -> None:
      last_node = self._head
      for c in word:
        last_node = last_node.get_child_or_create(c)
      last_node.mark_as_word(word)


    def search(self, word: str) -> bool:
      return self._search(word, 0, self._head, True)

    def _search(self, word, i, node, exact_match):
      if node is None:
        return False
      if i == len(word):
        if exact_match:
            return node._is_word
        else:
            return True
      c = word[i]
      child = node.get_child(c)
      return self._search(word, i + 1, child, exact_match)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix, 0, self._head, False)

class TrieNode:
  def __init__(self, letter):
    self._childs = {}
    self._word = None
  
  def get_child_or_create(self, letter):
    if not letter in self._childs:
      self._childs[letter] = TrieNode(letter)
    return self._childs[letter]
    
  def mark_as_word(self, word):
    self._word = word
  
  def get_child(self, letter):
    if letter in self._childs:
      return self._childs[letter]
    else:
      return None

from collections import deque

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        found = set()
        s = set(words)

        for w in words:
          trie.insert(w)
        for j in range(len(board)):
          for i in range(len(board[0])):
            local_used = set()
            accumulator = set()
            self._findWords(board, i, j, accumulator, trie._head, local_used)
            for w in accumulator:
              found.add(w)  

        return found

    def _findWords(self, board, i, j, accumulator, head, used):
      l = board[j][i]
      child = head.get_child(l)
      cur_set_entry = (i, j)
      used.add(cur_set_entry)
      if child:
        if child._word:
          accumulator.add(child._word)
        for adj in self._adj(i, j, board, used):
          self._findWords(board, adj[0], adj[1], accumulator, child, used)
      
      used.remove(cur_set_entry)

    def format_list(self, board, l):
      return list(map(lambda x: board[x[1]][x[0]], l))
    def _adj(self, curI, curJ, board, used):
        res = []
        if curJ - 1 >= 0:
            res.append((curI, curJ - 1))
        if curI - 1 >= 0:
            res.append((curI - 1, curJ))
        if curI + 1 < len(board[0]):
            res.append((curI + 1, curJ))
        if curJ + 1 < len(board):
            res.append((curI, curJ + 1))

        return filter(lambda x: x not in used, res)
        