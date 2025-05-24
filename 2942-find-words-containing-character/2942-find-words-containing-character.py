class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
      res = []
      for idx, w in enumerate(words):
        for c in w:
          if x == c:
            res += [idx]
            break
      return res