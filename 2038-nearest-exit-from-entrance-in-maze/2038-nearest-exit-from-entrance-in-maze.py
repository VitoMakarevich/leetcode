class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance_tuple = (entrance[0], entrance[1])
        pq = []
        self._directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self._target = entrance_tuple
        self._exits = self.calculate_exits(maze, entrance_tuple)
        if len(self._exits) == 0:
            return -1
        for v in self._exits:
            self.insert_into_pq(pq, v, 0)
        while pq:
            cur = heapq.heappop(pq)
            distance, pos, turn = cur
            i, j = pos
            if pos == self._target:
                return turn
            for adj in self.neighbors(maze, pos):
                maze[adj[0]][adj[1]] = '+'
                self.insert_into_pq(pq, adj, turn + 1)
        return -1
    def calculate_exits(self, maze, entrance):
        res = []
        max_i = len(maze) - 1
        max_j = len(maze[0]) - 1
        for i in range(len(maze)):
            if maze[i][0] == '.':
                res.append((i, 0))
            if maze[i][max_j] == '.':
                res.append((i, max_j))
        for j in range(len(maze[0])):
            if maze[0][j] == '.':
                res.append((0, j))
            if maze[max_i][j] == '.':
                res.append((max_i, j))
        return list(filter(lambda x: x != entrance, res))

    def calculate_exit_distance(self, coordinates):
        target_i, target_j = self._target
        i, j = coordinates
        dist = abs(i - target_i) + abs(j - target_j)
        return dist

    def insert_into_pq(self, pq, pos, turn):
        exit_distance = self.calculate_exit_distance(pos)
        heapq.heappush(pq, (turn + exit_distance, pos, turn))

    def neighbors(self, maze, position):
        i, j = position
        i_max = len(maze)
        j_max = len(maze[0])

        for di, dj in self._directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < i_max and 0 <= nj < j_max and maze[ni][nj] == '.':
                yield (ni, nj)
