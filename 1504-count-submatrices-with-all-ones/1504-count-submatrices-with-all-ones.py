class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        for i in range(m):
            row = [1 for _ in range(n)]
            for j in range(i, m):
                for k in range(n):
                    row[k] &= mat[j][k]
                res += self.num_one_row(row)
        return res
        
    def num_one_row(self, mat: List[int]) -> int:
        res = 0
        len = 0
        for i in mat:
            len = len + 1 if i else 0
            res += len
        return res