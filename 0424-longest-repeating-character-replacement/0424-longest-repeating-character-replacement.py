class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = 0
        res = 0
        elements = {}
        max_in_elements = 0
        for i, v in enumerate(s):
            size += 1
            elements[v] = elements.get(v, 0) + 1
            max_in_elements = max(elements[v], max_in_elements)
            if size - max_in_elements > k:
                size -= 1
                f = s[i - size]
                elements[f] -= 1
                if v == f:
                    max_in_elements -= 1
            res = max(res, size)
        return res