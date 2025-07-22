class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        store = {}

        res = inf
        for idx, card in enumerate(cards):
          if card in store:
            res = min(res, idx - store[card] + 1)
          store[card] = idx
        return res if res != inf else -1       