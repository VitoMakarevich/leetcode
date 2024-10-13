import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for v in nums:
            if len(pq) < k:
                heapq.heappush(pq, v)
            elif pq[0] < v:
                heapq.heappop(pq)
                heapq.heappush(pq, v)
        
        return pq[0]