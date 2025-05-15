class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        for x, y in points:
          points_set.add((x, y))
        res = inf
        # find and set to res
        for index, (x, y) in enumerate(points):
          for diagonal_index, (diagonal_x, diagonal_y) in enumerate(points):
            if diagonal_x != x and diagonal_y != y:
              
              top_side, bot_side = (x, y), (diagonal_x, diagonal_y)
              if top_side[1] < bot_side[1]:
                top_side, bot_side = bot_side, top_side

              other_top = (bot_side[0], top_side[1])
              other_bot = (top_side[0], bot_side[1])
              if other_top in points_set and other_bot in points_set:
                res = min(res, abs(top_side[0] - bot_side[0]) * abs(top_side[1] - bot_side[1]))
        return res if not res is inf else 0