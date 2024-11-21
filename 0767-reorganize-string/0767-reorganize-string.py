class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        print(counter)
        pq = []
        for character, count in counter.items():
            heapq.heappush(pq, (-count, character))
        res = ""
        highest = heapreplace(pq, (pq[0][0] + 1, pq[0][1]))
        res += highest[1]
        for v in s[1:]:
            prev = res[-1]
            new = pq[0][1]
            if new == prev:
                temp = heapq.heappop(pq)
                if len(pq) == 0:
                    return ""
                head_count = -pq[0][0]
                if head_count > 1:
                    new = heapq.heapreplace(pq, (pq[0][0] + 1, pq[0][1]))
                else:
                    new = heapq.heappop(pq)
                heapq.heappush(pq, temp)
            else:
                head_count = -pq[0][0]
                if head_count > 1:
                    new = heapq.heapreplace(pq, (pq[0][0] + 1, pq[0][1]))
                else:
                    new = heapq.heappop(pq)
            res += new[1]
        return res
