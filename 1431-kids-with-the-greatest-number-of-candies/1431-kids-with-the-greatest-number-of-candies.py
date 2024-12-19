class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = []
        for v in candies:
          res.append(v + extraCandies >= mx)
        return res
          