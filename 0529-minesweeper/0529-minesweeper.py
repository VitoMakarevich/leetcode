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
        queue = deque()
        queue.append((i, j))
        visited = set()
        while queue:
            for _ in range(len(queue)):
                item = queue.popleft()
                neighbors, bomb_counter = self._get_neighbors(item[0], item[1])
                if bomb_counter == 0:
                    self._board[item[0]][item[1]] = 'B'
                    for n in neighbors:
                        if n not in visited:
                            visited.add(n)
                            queue.append(n)
                else:
                    self._board[item[0]][item[1]] = str(bomb_counter)
                

    def _get_neighbors(self, i, j):
        neighbors = []
        bombs = 0
        for di, dj in self.directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < len(self._board) and 0 <= nj < len(self._board[0]):
                neighbors.append((ni, nj))
                bombs += 1 if self._board[ni][nj] == 'M' else 0
        
        return neighbors, bombs
