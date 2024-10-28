class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hq = []
        res = []
        to_delete = {}
        for i, v in enumerate(nums):
            heapq.heappush(hq, -v)
            if len(hq) >= k:
                idx_to_be_removed = i - k
                if idx_to_be_removed >= 0:
                # to be removed from PQ - value as in PQ
                    to_be_removed = -nums[i - k]
                    # increase remove counter by 1
                    to_delete[to_be_removed] = to_delete.get(to_be_removed, 0) + 1
                    while to_delete.get(hq[0], 0) > 0:
                        top = hq[0]
                        heapq.heappop(hq)
                        to_delete[top] -= 1

                res.append(-hq[0])
        
        return res
                