class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        index_position = [(idx, v) for idx, v in enumerate(dominoes) if v != '.']
        index_position = [(-1, 'L')] + index_position + [(len(dominoes), 'R')]

        res = list(dominoes)
        for (prev_idx, prev_value), (cur_idx, cur_value) in zip(index_position, index_position[1:]):
          if prev_value == cur_value:
            for index in range(prev_idx + 1, cur_idx):
              res[index] = cur_value
          elif cur_value == 'L' and prev_value == 'R':
            for index in range(prev_idx + 1, cur_idx):
              left_force = index - prev_idx
              right_force = cur_idx - index
              if left_force < right_force:
                res[index] = prev_value
              elif left_force > right_force:
                res[index] = cur_value
              else:
                res[index] = '.'
        return "".join(res)