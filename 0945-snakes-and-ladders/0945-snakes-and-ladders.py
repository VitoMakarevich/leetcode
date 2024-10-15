class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        visited = set()
        pq = deque()
        target = len(board) * len(board)
        is_root_snake_or_ladder = self._get_n(1, board)
        if is_root_snake_or_ladder == -1:
            pq.append(1)
        else:
            pq.append(is_root_snake_or_ladder)
        turn = 0
        visited = set()
        while len(pq) > 0:
            q_size = len(pq)
            for el in range(q_size):
                current_position = pq.popleft()
                if current_position not in visited:
                    if current_position == target:
                        return turn
                    for next_el in self._next_moves(current_position, target):
                        is_snake_or_ladder = self._get_n(next_el, board)
                        if is_snake_or_ladder != -1:
                            pq.append(is_snake_or_ladder)
                        else:
                            pq.append(next_el)
                    visited.add(current_position)
            turn += 1

        return -1



    def _next_moves(self, n, max_possible):
        logic_next_max_position = min(n + 6, max_possible * max_possible)
        return range(min(max_possible, n + 1), min(max_possible + 1, logic_next_max_position + 1))

    def _get_n(self, n, matrix):
        normalized_n = n - 1
        row = len(matrix) - int(floor(normalized_n / len(matrix))) - 1
        cell = 0
        is_this_row_normal_order = len(matrix) % 2 != row % 2
        if is_this_row_normal_order:
            cell = normalized_n % len(matrix)
        else:
            cell = len(matrix) - normalized_n % len(matrix) - 1
        return matrix[row][cell]
            