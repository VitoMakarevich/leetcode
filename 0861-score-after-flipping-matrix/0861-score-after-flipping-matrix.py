class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # first step flip left to right
        for row in grid:
            if row[0] != 1:
                for index, value in enumerate(row):
                    row[index] = 0 if value == 1 else 1
        
        vertical_size = len(grid)
        half_size = ceil(vertical_size / 2)
        for column in range(len(grid[0])):
            count_zeros = 0
            current_row = 0
            while count_zeros < half_size and current_row < vertical_size:
                if grid[current_row][column] == 0:
                    count_zeros += 1
                current_row += 1
            if count_zeros >= half_size:
                for row in grid:
                    row[column] = 0 if row[column] == 1 else 1
        
        res = 0
        for row in grid:
            number = 0
            for bit in row:
                number = (number << 1) | bit
            res += number

        return res