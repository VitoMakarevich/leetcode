class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        modulo = 10 ** 9 + 7
        y_to_x = defaultdict(list)
        for x, y in points:
          y_to_x[y].append(x)
        valid_y = {}
        combs = [comb(len(x), 2) for x in y_to_x.values()]
        sum_combs = sum(combs) ** 2 
        sum_squares = sum([c ** 2 for c in combs])
        res = ((sum_combs - sum_squares) // 2) % modulo
        return res
        
