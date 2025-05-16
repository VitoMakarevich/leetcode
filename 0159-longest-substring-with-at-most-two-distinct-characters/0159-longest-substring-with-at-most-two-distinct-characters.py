class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # 2 pointers
        # while - right += 1
        # for each iteration shift left until there is 2 keys
        # res = right - left + 1
        left, right = 0, 0
        storage = defaultdict(int)
        res = 0
        while right < len(s):
          storage[s[right]] += 1
          while len(storage) > 2:
            storage[s[left]] -= 1
            if storage[s[left]] == 0:
              del storage[s[left]]
            left += 1
          res = max(res, right - left + 1)
          right += 1
        return res