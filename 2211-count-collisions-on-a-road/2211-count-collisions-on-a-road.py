class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        res = 0
        for d in directions:
          if not stack:
            stack.append(d)
            continue
          prev_cur = stack[-1] + d
          match prev_cur:
            case 'SS' | 'LS' | 'SR' | 'LR':
              stack.pop()
              stack.append(d)
            case 'SL' :
              res += 1
            case 'RR':
              stack.append(d)
            case 'RS' | 'RL':
              if prev_cur == 'RL':
                res += 1
              while stack and stack[-1] == 'R':
                res += 1
                stack.pop()
              stack.append('S')
        return res

