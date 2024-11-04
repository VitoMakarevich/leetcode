class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance_tuple = (entrance[0], entrance[1])
        pq = []
        self._directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self._exits = self.calculate_exits(maze, entrance_tuple)
        if len(self._exits) == 0:
            return -1
        visited = set()
        self.insert_into_pq(pq, entrance_tuple, 0)
        while pq:
            cur = heapq.heappop(pq)
            distance, pos, turn = cur
            i, j = pos
            if pos != entrance_tuple and (
                i == 0 or
                i == len(maze) - 1 or
                j == 0 or
                j == len(maze[0]) - 1
            ):
                return turn
            for adj in self.neighbors(maze, pos, visited):
                visited.add(adj)
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
        res = []
        for v in self._exits:
            i, j = coordinates
            exit_i, exit_j = v
            dist = sqrt(pow(abs(i - exit_i), 2) + pow(abs(j - exit_j), 2))
            res.append(dist)

    
        return min(res)
        

    def insert_into_pq(self, pq, pos, turn):
        exit_distance = self.calculate_exit_distance(pos)
        heapq.heappush(pq, (turn + exit_distance, pos, turn))

    def neighbors(self, maze, position, visited):
        i, j = position
        i_max = len(maze)
        j_max = len(maze[0])

        for di, dj in self._directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < i_max and 0 <= nj < j_max and (ni, nj) not in visited and maze[ni][nj] == '.':
                yield (ni, nj)
