class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0 for i in range(len(temperatures))]
        for i, v in enumerate(temperatures):
            if len(stack) == 0 or stack[-1][1] >= v:
                stack.append((i, v))
            elif stack[-1][1] < v:
                while len(stack) > 0 and stack[-1][1] < v:
                    day, temp = stack.pop()
                    res[day] = i - day
                    
                stack.append((i, v))
            # print(f"i={i}, stack={stack}")

        return res