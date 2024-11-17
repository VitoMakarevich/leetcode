class Solution:
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self._board = board 
        i, j = click
        click_item = board[i][j]
        if click_item == 'M':
            board[i][j] = 'X'
        elif click_item == 'E':
            self._open(i, j)
        return self._board


    def _open(self, i, j):
        if not (self._board[i][j] == 'E'):
            return
        neighbors, bomb_counter = self._get_neighbors(i, j)
        if bomb_counter == 0:
            self._board[i][j] = 'B'
            for n in neighbors:
                self._open(n[0], n[1])
        else:
            self._board[i][j] = str(bomb_counter)

    def _get_neighbors(self, i, j):
        neighbors = []
        bombs = 0
        for di, dj in self.directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < len(self._board) and 0 <= nj < len(self._board[0]):
                neighbors.append((ni, nj))
                bombs += 1 if self._board[ni][nj] == 'M' else 0
        
        return neighbors, bombs
