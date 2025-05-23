class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        s = deque()
        for idx in range(len(heights)):
          while s and heights[idx] >= heights[s[-1]]:
            s.pop()
          s.append(idx)
        return list(s)