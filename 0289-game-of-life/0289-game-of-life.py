class Solution:
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._board = board
        modifications = {}
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                is_alive = self._board[i][j] == 1
                if is_alive:
                    alive_neighbors_count, dead_neighbors = self._get_neighbors(i, j)
                    if alive_neighbors_count < 2 or alive_neighbors_count > 3:
                        modifications[(i, j)] = 0
                    for dead in dead_neighbors:
                        if not dead in visited:
                            visited.add(dead)
                            if self._get_neighbors(dead[0], dead[1])[0] == 3:
                                modifications[dead] = 1
        for coordinates, new_state in modifications.items():
            i, j = coordinates
            self._board[i][j] = new_state

    def _get_neighbors(self, i, j):
        dead_neighbors = []
        alive_neighbors_count = 0
        for di, dj in self.directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < len(self._board) and 0 <= nj < len(self._board[0]):
                nbr = self._board[ni][nj]
                if nbr == 1:
                    alive_neighbors_count += 1
                else:
                    dead_neighbors.append((ni, nj))
        
        return alive_neighbors_count, dead_neighbors