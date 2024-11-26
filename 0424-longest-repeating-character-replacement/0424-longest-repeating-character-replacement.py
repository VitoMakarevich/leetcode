class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = 0
        q = deque()
        res = 0
        elements = {}
        for v in s:
            size += 1
            elements[v] = elements.get(v, 0) + 1
            max_in_elements = max(elements.values())
            if size - max_in_elements > k:
                size -= 1
                elements[q.popleft()] -= 1
            q.append(v)
            res = max(res, size)
        return res