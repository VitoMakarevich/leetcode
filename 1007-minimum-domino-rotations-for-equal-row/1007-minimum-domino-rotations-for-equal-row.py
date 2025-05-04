class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
      def check_item(target):
        top_side = 0
        bot_side = 0
        for top, bottom in zip(tops, bottoms):
          if top != target and bottom != target:
            return -1
          elif top != target:
            bot_side += 1
          elif bottom != target:
            top_side += 1
        return min(top_side, bot_side)
      res = check_item(tops[0])
      if res != -1 or tops[0] == bottoms[0]:
        return res
      else:
        return check_item(bottoms[0])
