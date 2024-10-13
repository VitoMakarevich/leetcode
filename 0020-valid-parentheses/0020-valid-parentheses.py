class Solution:
    _open = {"{", "[", "("}
    _close = {"}", "]", ")"}
    _pairs = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in self._open:
                stack.append(c)
            elif c in self._close and len(stack) > 0 and stack[-1] == self._pairs[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        