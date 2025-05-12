class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets = list(filter(lambda x: target[0] >= x[0] and target[1] >= x[1] and target[2] >= x[2], triplets))
        position_match_0 = False
        position_match_1 = False
        position_match_2 = False
        target_x, target_y, target_z = target
        for x, y, z in triplets:
          position_match_0 = x == target_x or position_match_0
          position_match_1 = y == target_y or position_match_1
          position_match_2 = z == target_z or position_match_2
          if position_match_0 and position_match_1 and position_match_2:
            return True
        return False
