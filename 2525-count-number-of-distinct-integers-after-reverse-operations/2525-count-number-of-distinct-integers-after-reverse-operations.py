class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)
        unique = list(s)
        for v in unique:
            s.add(self.reverse(v))
        return len(s)

    def reverse(self, n):
        return int(str(n)[::-1])