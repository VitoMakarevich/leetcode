class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = deque()

        push_i = 0
        pop_i = 0
        while push_i < len(pushed) or pop_i < len(popped):
          if len(s) > 0 and pop_i < len(popped) and s[-1] == popped[pop_i]:
            s.pop()
            pop_i += 1
          elif len(pushed) > 0 and (len(s) == 0 or push_i < len(pushed)):
            s.append(pushed[push_i])
            push_i += 1
          else:
            return False
        return push_i == len(pushed) and pop_i == len(popped) 