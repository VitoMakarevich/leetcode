class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        store = defaultdict(int)
        for day_resp in responses:
          uniq = set(day_resp)
          for item in uniq:
            store[item] += 1
        minimal = (0, 'a')
        for key, value in store.items():
          minimal = min(minimal, (-value, key))
        return minimal[1]