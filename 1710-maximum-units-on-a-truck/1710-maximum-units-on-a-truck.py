class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        res = 0
        for boxes, units_per_box in boxTypes:
          if truckSize == 0:
            return res
          else:
            boxes_to_take = min(truckSize, boxes)
            res += boxes_to_take * units_per_box
            truckSize -= boxes_to_take
        return res