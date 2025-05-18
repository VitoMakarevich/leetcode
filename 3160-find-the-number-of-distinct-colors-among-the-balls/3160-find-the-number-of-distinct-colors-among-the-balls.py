class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = 0
        storage = {}
        color_count = defaultdict(int)
        res = []
        for i, color in queries:
          if not i in storage:
            storage[i] = color
            color_count[color] += 1
            res.append(len(color_count))
          else:
            prev = storage[i]
            color_count[prev] -= 1
            if color_count[prev] == 0:
              del color_count[prev]
            storage[i] = color
            color_count[color] += 1
            res.append(len(color_count))
        return res