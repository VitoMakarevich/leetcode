class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        left_map = defaultdict(int)
        right_map = defaultdict(int)
        for c1, c2 in zip(s, t):
            if not c2 in left_map and not c1 in right_map:
              left_map[c2] = c1
              right_map[c1] = c2
            elif left_map.get(c2) != c1 or right_map.get(c1) != c2:
              return False

        return True