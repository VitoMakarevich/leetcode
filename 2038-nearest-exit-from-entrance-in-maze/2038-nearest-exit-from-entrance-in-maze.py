class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance_tuple = (entrance[0], entrance[1])
        q = deque([entrance_tuple])
        visited = set()
        turn = 0
        while q:
            for v in range(len(q)):
                pos = q.popleft()
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
                    q.append(adj)
            turn += 1
        return -1


    def neighbors(self, maze, position, visited):
        i, j = position
        i_max = len(maze)
        j_max = len(maze[0])

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < i_max and 0 <= nj < j_max and (ni, nj) not in visited and maze[ni][nj] == '.':
                yield (ni, nj)
