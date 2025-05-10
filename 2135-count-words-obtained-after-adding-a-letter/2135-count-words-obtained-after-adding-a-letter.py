class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_words = set()
        for w in startWords:
          start_words.add("".join(sorted(w)))

        res = 0
        for target in targetWords:
          sorted_target = "".join(sorted(target))
          for i in range(0, len(target)):
            candidate = sorted_target[:i] + sorted_target[i + 1:]
            if candidate in start_words:
              res += 1
              break
        return res
 