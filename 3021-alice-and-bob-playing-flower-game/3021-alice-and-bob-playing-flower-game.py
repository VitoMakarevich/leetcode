class Solution:
    def flowerGame(self, n: int, m: int) -> int:
      n_even = n // 2 # 1
      n_odd = n - n_even # 2
      m_even = m // 2 # 1
      m_odd = m - m_even # 1

      res = n_even * m_odd + n_odd * m_even
      return res
    
