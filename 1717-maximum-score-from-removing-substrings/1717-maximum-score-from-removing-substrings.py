class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        initial_s = s
        bigger_pair = 'ab' if x > y else 'ba'
        smaller_pair = 'ba' if bigger_pair == 'ab' else 'ab'
        bigger_price = max(x, y)
        smaller_price = min(x, y)
        res = 0
        
        def remove_target(pair, price):
          res = 0
          q = deque()
          for c in s:
            if not q or q[-1] + c != pair:
              q.append(c)
            else:
              q.pop()
              res += price
          return res, ''.join(q)
        local_res, s = remove_target(bigger_pair, bigger_price)
        res += local_res
        res += remove_target(smaller_pair, smaller_price)[0]
        return res
        