class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self._dictionary = defaultdict(set)
        for v in dictionary:
          abbr = self._get_abbr(v)
          self._dictionary[abbr].add(v)
    def _get_abbr(self, w):
      if len(w) == 1 or len(w) == 2:
        return w
      else:
        return f"{w[0]}{len(w) - 2}{w[-1]}"

    def isUnique(self, word: str) -> bool:
      abbr = self._get_abbr(word)
      abbr_in_dictionary = abbr in self._dictionary
      if not abbr_in_dictionary:
        return True
      word_in_dictionary = word in self._dictionary[abbr]
      return word_in_dictionary and len(self._dictionary[abbr]) == 1
    
    # abbr word res
    # 1    0    0
    # 0    0    1
    # 1    1    1
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)