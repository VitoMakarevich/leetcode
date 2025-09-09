class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
      mod = 10**9 + 7
      dp = [{'share': 0, 'forget': 0} for _ in range(n)]
      cur = 0
      new = 1
      dp[0]['share'] = 1
      for i in range(n):
        new = dp[i]['share'] - dp[i]['forget'] if i != 0 else new
        cur = max(cur + new, 0) % mod
        if cur == 0:
          return 0
        share_up_to = min(n, i + forget)
        for share_point in range(i + delay, share_up_to):
          dp[share_point]['share'] += dp[i]['share']
        if i + forget < n:
          dp[i + forget]['forget'] += dp[i]['share']
        # print(f'dp={dp[i]}, cur={cur}, new={new}')
      return cur