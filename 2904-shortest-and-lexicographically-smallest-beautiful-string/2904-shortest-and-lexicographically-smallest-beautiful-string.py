class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        res = None
        for l in range(n):
            if s[l] == '0':
                continue 
            count_ones = 0
            for r in range(l, n):
                if s[r] == '1':
                    count_ones += 1
                if count_ones == k:
                    candidate = s[l:r+1]
                    if res is None or len(candidate) < len(res) or (len(candidate) == len(res) and candidate < res):
                        res = candidate
                    break 
                elif count_ones > k:
                    break
        return res if res else ""
