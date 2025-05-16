class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # bf
        output = []
        distances = [[0] * len(words) for i in range(len(words))]
        for idx  in range(len(words)):
          for next_idx in range(len(words)):
            distances[idx][next_idx] = self.hamming_distance(words[idx], words[next_idx])

        @cache
        def dp(cur_word_idx):
          if cur_word_idx == len(words) - 1:
            return [words[cur_word_idx]]

          ans = []
          for next_idx in range(cur_word_idx + 1, len(words)):
            if len(words[cur_word_idx]) == len(words[next_idx]) and groups[cur_word_idx] != groups[next_idx] and distances[cur_word_idx][next_idx] == 1:
              next_res = dp(next_idx)
              if len(next_res) > len(ans):
                ans = next_res
          return [words[cur_word_idx]] + ans

        for start_idx in range(len(words)):
          ans = dp(start_idx)
          if len(ans) > len(output):
            output = ans

        return output
           
    

    def hamming_distance(self, word1, word2):
      if len(word1) != len(word2):
        return inf
      dist = 0
      for i in range(len(word1)):
        dist += int(word1[i] != word2[i])
      return dist