class Solution:
    def partitionString(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        return max(counter.values())