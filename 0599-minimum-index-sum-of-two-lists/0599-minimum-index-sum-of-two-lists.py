class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
      first_map = self._create_position_hash(list1)
      second_map = self._create_position_hash(list2)
      min_diff = inf
      min_diff_values = []
      for value, position in first_map.items():
        if value in second_map:
          if position + second_map[value] < min_diff:
            min_diff = position + second_map[value]
          if position + second_map[value] <= min_diff:
            min_diff_values.append(value)
      return min_diff_values

    def _create_position_hash(self, input):

        output = {}
        for index, s in enumerate(input):
          if s not in output:
            output[s] = index
        return output
