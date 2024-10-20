class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = deque([asteroids[0]])
        for i in range(1, len(asteroids)):
            cur = asteroids[i]
            while res:
                last = res.pop()
                if cur < 0 and last > 0 and abs(cur) > last:
                    continue
                else:
                    res.append(last)
                    break
            if res:
                last = res.pop()
                if cur < 0 and last > 0 and cur == -last:
                    # do nothing
                    pass
                elif (last < 0 and cur < 0) or (last > 0 and cur > 0):
                    res.append(last)
                    res.append(cur)
                elif cur > 0 and last < 0:
                    res.append(last)
                    res.append(cur)
                else:
                    res.append(last)
            else:
                res.append(cur)
            # print(f"i={i}, res={list(res)}")

        return list(res)