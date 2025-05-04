class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = defaultdict(int)
        for domino in dominoes:
            dom = tuple(sorted(domino))
            pairs[dom] += 1
        res = 0
        for count in pairs.values():
          res += math.comb(count, 2)
        return res
