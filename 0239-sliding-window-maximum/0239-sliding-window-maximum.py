class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hq = []
        res = []
        to_delete = {}
        for i, v in enumerate(nums):
            # print(hq)
            heapq.heappush(hq, -v)
            if len(hq) >= k:
                idx_to_be_removed = i - k
                if idx_to_be_removed >= 0:
                # to be removed from PQ - value as in PQ
                    to_be_removed = -nums[i - k]
                    # increase remove counter by 1
                    to_delete[to_be_removed] = to_delete.get(to_be_removed, 0) + 1
                    # print(f"i={i}, to_be_removed={to_be_removed}, to_delete={to_delete}, hq={hq}, {to_delete.get(-hq[0], 0)}")
                    while len(hq) > 0 and to_delete.get(hq[0], 0) > 0:
                        # print(i, to_delete, hq, to_delete.get(hq[0], 0), hq[0])
                        top = hq[0]
                        heapq.heappop(hq)
                        to_delete[top] -= 1
                # print(hq)

                res.append(-hq[0])
        
        return res
                