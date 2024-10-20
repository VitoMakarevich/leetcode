class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = deque([asteroids[0]])
        for i in range(1, len(asteroids)):
            cur = asteroids[i]
            while res:
                last = res.pop()
                if not(cur < 0 and last > 0 and abs(cur) > last):
                    res.append(last)
                    break
            if res:
                last = res[-1]
                # if equal but different signs
                if cur < 0 and last > 0 and cur == -last:
                    # remove last item in deque
                    res.pop()
                # if both same sign or + follows -
                elif ((last < 0 and cur < 0) or (last > 0 and cur > 0)) or (cur > 0 and last < 0):
                    res.append(cur)
            else:
                res.append(cur)

        return list(res)