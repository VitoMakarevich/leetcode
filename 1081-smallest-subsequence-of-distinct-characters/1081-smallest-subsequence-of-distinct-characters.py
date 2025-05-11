class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)

        visited = set()
        stack = []
        for c in s:
          counter[c] -= 1
          if c in visited:
            continue
          while stack and stack[-1] > c and counter[stack[-1]] > 0:
            visited.discard(stack.pop())
          stack.append(c)
          visited.add(c)
        return "".join(stack)