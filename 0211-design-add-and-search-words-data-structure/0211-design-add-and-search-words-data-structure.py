class WordDictionary:

    def __init__(self):
      self._head = TrieNode(None)

    def addWord(self, word: str) -> None:
      last_node = self._head
      for c in word:
        last_node = last_node.get_child_or_create(c)
      last_node.mark_as_word()

    def search(self, word: str) -> bool:
      return self._search(word, 0, self._head)
    def _search(self, word, i, node):
      c = word[i]
      childs = node.get_childs(c)
      if i == len(word) - 1:
        for child in childs:
          if child._is_word:
            return True
        return False
      else:  
        for child in childs:
          if self._search(word, i + 1, child):
            return True
      return False

any_char = '.'
empty_list = []

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
  
  def get_childs(self, letter):
    if letter == any_char:
      return self._childs.values()
    elif letter in self._childs:
      return [self._childs[letter]]
    else:
      return empty_list

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)