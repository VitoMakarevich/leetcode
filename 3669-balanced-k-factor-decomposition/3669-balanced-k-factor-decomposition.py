class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        divs = self.get_divisors(n)
        best_diff = float('inf')
        best = []
        
        def dfs(start, prod, path):
            nonlocal best_diff, best
            if len(path) == k:
                if prod == n:
                    diff = max(path) - min(path)
                    if diff < best_diff:
                        best_diff = diff
                        best = path[:]
                return
            
            for i in range(start, len(divs)):
                val = divs[i]
                new_prod = prod * val
                if new_prod > n:
                    break
                if n % new_prod != 0:
                    continue
                
                path.append(val)
                dfs(i, new_prod, path)
                path.pop()
        
        dfs(0, 1, [])
        return best
    
    def get_divisors(self, n: int) -> List[int]:
        divs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divs.append(i)
                if i != n // i:
                    divs.append(n // i)
            i += 1
        divs.sort()
        return divs