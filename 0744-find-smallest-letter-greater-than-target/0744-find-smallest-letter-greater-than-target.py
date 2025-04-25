class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
      point = self.bisect_right(letters, target)
      return letters[0] if point >= len(letters) else letters[point]
    
    def bisect_right(self, letters, target):
      low, high = 0, len(letters)
      while low < high:
        mid = (low + high) // 2
        if letters[mid] <= target:
          low = mid + 1
        else:
          high = mid
      return low