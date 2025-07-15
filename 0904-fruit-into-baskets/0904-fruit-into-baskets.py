class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(list)
        res = 0
        left = 0
        first = None
        second = None
        for right in range(len(fruits)):
          baskets[fruits[right]].append(right)
          if first == None:
            first = fruits[right]
          elif second == None and not first == fruits[right]:
            second = fruits[right]
          if len(baskets) == 3:
            if baskets[first][-1] > baskets[second][-1]:
              last_pos = bisect_right(baskets[first], baskets[second][-1])
              baskets[first] = baskets[first][last_pos:]
              del baskets[second]
              left = baskets[first][0]
              second = fruits[right]
            else:
              last_pos = bisect_right(baskets[second], baskets[first][-1])
              baskets[second] = baskets[second][last_pos:]
              del baskets[first]
              left = baskets[second][0]
              first = second
              second = fruits[right]
            

          res = max(res, right - left + 1)
        return res
              