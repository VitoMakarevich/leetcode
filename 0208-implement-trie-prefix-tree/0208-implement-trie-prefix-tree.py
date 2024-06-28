class Trie:

    def __init__(self):
        self._head = TrieNode(None)
        

    def insert(self, word: str) -> None:
      last_node = self._head
      for c in word:
        last_node = last_node.get_child_or_create(c)
      last_node.mark_as_word()


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
    self._is_word = False
  
  def get_child_or_create(self, letter):
    if not letter in self._childs:
      self._childs[letter] = TrieNode(letter)
    return self._childs[letter]
    
  def mark_as_word(self):
    self._is_word = True
  
  def get_child(self, letter):
    if letter in self._childs:
      return self._childs[letter]
    else:
      return None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)