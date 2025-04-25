class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = self.bisect_left(arr, x) - 1
        right = left + 1
        res = deque()

        while left >= 0 and right < len(arr) and len(res) < k:
            left_diff = abs(arr[left] - x)
            right_diff = abs(arr[right] - x)
            if left_diff <= right_diff:
                res.appendleft(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1

        while len(res) < k and left >= 0:
            res.appendleft(arr[left])
            left -= 1
        while len(res) < k and right < len(arr):
            res.append(arr[right])
            right += 1

        return list(res)

            
        
    
    def bisect_left(self, arr, target):
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low