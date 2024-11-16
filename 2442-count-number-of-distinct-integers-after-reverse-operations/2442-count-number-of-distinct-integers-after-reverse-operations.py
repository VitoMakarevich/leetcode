class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)
        new_s = set()
        for v in s:
            new_s.add(self.reverse(v))
        return len(new_s.union(s))

    def reverse(self, n):
        return int(str(n).rstrip("0")[::-1])