class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = [{} for i in range(len(triangle))]
        return self._min(triangle, 0, 0, cache, len(triangle) - 1)

    def _min(self, triangle, level, i, cache, max_level):
        level_cache = cache[level]
        if not i in level_cache:
            if level == max_level:
                level_cache[i] = triangle[level][i]
            else:
                cur_i = triangle[level][i] + self._min(triangle, level + 1, i, cache, max_level)
                if i < level + 1:
                    next_i = triangle[level][i] + self._min(triangle, level + 1, i + 1, cache, max_level)
                    level_cache[i] = min(cur_i, next_i)
                else:
                    level_cache[i] = cur_i
        return level_cache[i]
    


        
