class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        nums = ["1"]
        factorials = [1]
        for i in range(1, n):
          factorials.append(factorials[i - 1] * i)
          nums.append(str(i + 1))
        
        res = []
        for i in range(n - 1, -1, -1):
          idx = k // factorials[i]
          k -= idx * factorials[i]
          res.append(nums[idx])
          del nums[idx]
        return "".join(res)
        
        
