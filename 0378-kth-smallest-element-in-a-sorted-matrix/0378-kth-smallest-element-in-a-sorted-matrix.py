class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        for row in range(min(len(matrix), k)):
            heapq.heappush(pq, (matrix[row][0], row, 0))
        
        while k > 0:
            value, row, column = heapq.heappop(pq)
            if column + 1 < len(matrix[0]):
                heapq.heappush(pq, (matrix[row][column + 1], row, column + 1))
            k -= 1
        return value