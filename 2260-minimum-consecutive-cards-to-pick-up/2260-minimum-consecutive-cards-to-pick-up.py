class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        store = defaultdict(list)
        for idx, card in enumerate(cards):
          store[card].append(idx)
        res = inf
        for indexes in store.values():
          for i1, i2 in pairwise(indexes):
            res = min(res, i2 - i1 + 1)
        return res if res != inf else -1