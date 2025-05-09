class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self._internal(n, k -  1)
    
    def _internal(self, n, k):
        if n == 1:
            return 0
        n_level_size = 2 ** (n - 1)
        is_inverse = int(k >= (n_level_size / 2))
        pos_in_prev = k % (n_level_size / 2)
        res = self._internal(n - 1, pos_in_prev)
        return is_inverse ^ res