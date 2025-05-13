class Solution:
    MOD = 10 ** 9 + 7
    def lengthAfterTransformations(self, s: str, t: int) -> int:
      res = 0
      cnt = [0] * 26
      for ch in s:
        cnt[ord(ch) - ord("a")] += 1
      for r in range(t):
        nxt = [0] * 26
        nxt[0] = cnt[25]
        nxt[1] = (cnt[25] + cnt[0]) % Solution.MOD
        for i in range(2, 26):
          nxt[i] = cnt[i - 1]
        cnt = nxt
      return sum(cnt) % Solution.MOD
      return res