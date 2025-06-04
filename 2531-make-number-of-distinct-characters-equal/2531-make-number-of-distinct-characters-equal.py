class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
      counter1 = Counter(word1)
      counter2 = Counter(word2)

      if len(counter1) == len(counter2):
        if len(counter1) == 1 and (counter1[word1[0]] == 1 or counter2[word2[0]] == 1):
          return False
        return True
      diff = abs(len(counter1) - len(counter2))
      if diff > 2:
        return False
      bigger_counter = counter1 if len(counter1) > len(counter2) else counter2
      smaller_counter = counter1 if len(counter1) < len(counter2) else counter2
      if diff == 2:
        for char2, count2 in bigger_counter.items():
          for char1, count1 in smaller_counter.items():
            if count2 > 1 and count1 == 1 and not char2 in bigger_counter:
              return True
        return False
      else:
        for char1, count1 in bigger_counter.items():
          if char1 in smaller_counter:
            continue
          # scenario 1:
          # give char that exists once in bigger - and missing in smaller - and take one from smaller that has count > 1 - and exists in bigger
          # scenario 2:
          # give char from bigger with cnt == 1 and missing in smaller - and take one from smaller with cnt > 1 and missing in bigger
          for char2, count2 in smaller_counter.items():
            if count1 > 1 and not char1 in smaller_counter and char2 in bigger_counter:
              return True
            if not char1 in smaller_counter and count2 == 1 and char2 in bigger_counter:
              return True
            if count1 == 1 and not char1 in smaller_counter and count2 > 1 and not char2 in bigger_counter:
              return True
            
        return False
            