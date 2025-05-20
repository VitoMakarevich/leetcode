class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        output = list(nums)
        nums += [inf]
        nums_with_idx = [(val, idx) for idx, val in enumerate(nums)]
        nums_with_idx.sort()
        group_indexes = [nums_with_idx[0][1]]
        group_values = [nums_with_idx[0][0]]
        for idx, (val, old_idx) in enumerate(nums_with_idx[1:], start = 1):
          if val - nums_with_idx[idx - 1][0] > limit:
            group_indexes.sort()
            for new_idx, new_val in zip(group_indexes, group_values):
              output[new_idx] = new_val
            group_indexes = [old_idx]
            group_values = [val]
          else:
            group_indexes.append(old_idx)
            group_values.append(val)
        
        return output