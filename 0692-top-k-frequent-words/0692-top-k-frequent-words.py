class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        q = []
        if k == 1:
          cur_min = ((-counter[words[0]], words[0]), words[0])
          for word, count in counter.items():
            cur = ((-count, word), word)
            if cur < cur_min:
              cur_min = cur
          q.append(cur_min)
        else:
          for word, count in counter.items():
            item = ((count, self.negate_str(word)), word)
            if len(q) == k and item > q[0]:
                heapq.heapreplace(q, item)
            elif len(q) < k:
              heapq.heappush(q, item)

        res_q = []
        while len(q):
          nxt = heapq.heappop(q)
          heapq.heappush(res_q, ((-nxt[0][0], nxt[1]), nxt[1]))
        res = []
        while len(res_q):
          res.append(heapq.heappop(res_q)[1])
        return res
    def negate_str(self, string):
      return tuple(-ord(c) for c in string)