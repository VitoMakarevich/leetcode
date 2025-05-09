class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        prev = arr[0]
        min_diff = inf
        min_v = []
        for index in range(1, len(arr)):
          if arr[index] - arr[index - 1] < min_diff:
            min_v = []
          if arr[index] - arr[index - 1] == min_diff:
            min_v.append([arr[index - 1], arr[index]])
        return min_v