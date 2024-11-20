class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 2 solutions possible:
        # 1. with 2 heaps - time complexity O((n + k) logK), memory - O(k)
        # 2. with binary search - logN + k, memory - O(1)
        # bisect is clear winner
        res = deque()
        left = 0
        right = len(arr)
        while left < right:
            mid = floor((right - left)/2 + left)
            if x < arr[mid]:
                right = mid
            elif x > arr[mid]:
                left = mid + 1
            else:
                left = mid
                break
        left = left - 1
        right = left + 1
        while len(res) < k:
            if left >= 0 and right < len(arr):
                left_diff = abs(arr[left] - x)
                right_diff = abs(arr[right] - x)
                if left_diff <= right_diff:
                    res.appendleft(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            elif left < 0:
                res.append(arr[right])
                right += 1
            else:
                res.appendleft(arr[left])
                left -= 1
        return list(res)


        