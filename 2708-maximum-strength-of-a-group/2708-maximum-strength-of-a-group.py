class Solution:
    def maxStrength(self, nums: List[int]) -> int:
      negative = deque()
      positive = deque()
      zeros = deque()
      for v in nums:
        if v < 0:
          negative.append(v)
        elif v > 0:
          positive.append(v)
        else:
          zeros.append(v)
      
      if len(negative) >= 2:
        negative_divider = max(negative) if len(negative) % 2 == 1 else 1
        
        return prod(negative) // negative_divider * prod(positive)
      if len(positive) > 0:
        return prod(positive)
      if len(zeros):
        return 0
      return negative[0]

      
      