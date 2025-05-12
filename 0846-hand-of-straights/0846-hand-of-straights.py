class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
          return False
        
        s_dict = SortedDict()
        for card in hand:
          if not card in s_dict:
            s_dict[card] = 0
          s_dict[card] += 1
        
        group_count = len(hand) // groupSize

        for _ in range(group_count):
          start, count = s_dict.peekitem(0)
          if count == 1:
            del s_dict[start]
          else:
            s_dict[start] -= 1
          for target in range(start + 1, start + groupSize):
            if not target in s_dict:
              return False
            if s_dict[target] == 1:
              del s_dict[target]
            else:
              s_dict[target] -= 1
        return True

        
