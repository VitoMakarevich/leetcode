EMPTY = 2147483647
TODO = -1
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gates = []
        for i in range(len(rooms)):
          for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
              gates.append((i, j))

        q = deque(gates)
        c = 0
        while len(q):
          for m in range(len(q)):
            i, j = q.popleft()
            
            rooms[i][j] = c
            for neigh_i, neigh_j in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
              if neigh_i >= 0 and neigh_j >= 0 and neigh_i < len(rooms) and neigh_j < len(rooms[0]) and rooms[neigh_i][neigh_j] == EMPTY:
                rooms[neigh_i][neigh_j] = TODO
                q.append((neigh_i, neigh_j))
          c += 1
        