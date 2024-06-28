class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            r = len(matrix[i]) - 1
            l = 0
            arr = matrix[i]
            check = True
            if target > arr[len(arr) - 1]:
                check = False
            while l <= r and check:
                mid = l + (r - l) // 2

                if arr[mid] == target:
                    return True

                elif arr[mid] < target:
                    l = mid + 1

                else:
                    r = mid - 1

        return False