class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = []
        res = num
        for digit in num:
            while q and k > 0 and q[-1] > digit:
                q.pop()
                k -= 1
            q.append(digit)
        
        q = q[:-k] if k > 0 else q
        
        result = ''.join(q).lstrip('0')
        
        return result if result else '0'  