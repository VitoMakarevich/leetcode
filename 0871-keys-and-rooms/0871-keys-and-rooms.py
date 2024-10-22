class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        queue = deque([0])
        while queue:
            for i in range(len(queue)):
                current = queue.popleft()
                keys = rooms[current]
                for key in keys:
                    if key not in visited:
                        visited.add(key)
                        queue.append(key)
        
        return len(visited) == len(rooms)

        
            

