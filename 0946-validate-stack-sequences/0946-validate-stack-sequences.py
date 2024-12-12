class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = deque()

        push_i = 0
        pop_i = 0
        l_pushed = len(pushed)
        l_popped = len(popped)
        while push_i < l_pushed or pop_i < l_popped:
          if len(s) > 0 and pop_i < l_popped and s[-1] == popped[pop_i]:
            s.pop()
            pop_i += 1
          elif l_pushed > 0 and (len(s) == 0 or push_i < l_pushed):
            s.append(pushed[push_i])
            push_i += 1
          else:
            return False
        return push_i == l_pushed and pop_i == l_popped