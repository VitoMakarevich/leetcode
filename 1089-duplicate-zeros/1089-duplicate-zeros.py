class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        zeroes_found = arr.count(0)
        l = len(arr) - 1
        for i in range(l, -1, -1):
          if i + zeroes_found <= l:
            arr[i + zeroes_found] = arr[i]
          if arr[i] == 0:
            zeroes_found -= 1
            if i + zeroes_found <= l:
              arr[i + zeroes_found] = 0
        return arr