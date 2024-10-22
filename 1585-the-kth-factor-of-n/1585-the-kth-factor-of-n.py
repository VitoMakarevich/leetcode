class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        smol, big = [], []
        for i in range(1, int(sqrt(n))+1):
            if n%i==0:
                smol.append(i)
                big.append(n//i)
        if smol[-1]==big[-1]: big.pop()
        factors=smol+big[::-1]
        return -1 if len(factors)<k else factors[k-1]