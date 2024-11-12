class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        available_tickets = {}
        graph = {}
        path = deque()
        path.append('JFK')
        for t in tickets:
            ticket = (t[0], t[1])
            available_tickets[ticket] = available_tickets.get(ticket, 0) + 1
            source, target = t
            if source not in graph:
                graph[source] = []
            graph[source].append(target)
        res = []
        self._dfs(available_tickets, graph, len(tickets) + 1, res, 'JFK', path)
        return res[0]
    def _dfs(self, available_tickets, graph, target_tickets, res, node, path):

        if len(path) == target_tickets:
            if len(res) == 0:
                res.append(list(path))
            else:
                res[0] = self._compare_paths(res[0], path)

        if node in graph:
            for adj in graph[node]:
                ticket = (node, adj)
                if available_tickets.get(ticket, 0) > 0:
                    available_tickets[ticket] -= 1
                    path.append(adj)
                    self._dfs(available_tickets, graph, target_tickets, res, adj, path)
                    available_tickets[ticket] += 1
                    path.pop()


    def _compare_paths(self, existing, candidate):
        lst_candidate = list(candidate)
        cur_word = 0
        cur_pos_in_word = 0
        while existing[cur_word][cur_pos_in_word] == lst_candidate[cur_word][cur_pos_in_word] and cur_word < len(existing) - 1:
            if cur_pos_in_word < 2:
                cur_pos_in_word += 1
            else:
                cur_word += 1
                cur_pos_in_word = 0
        if existing[cur_word][cur_pos_in_word] < lst_candidate[cur_word][cur_pos_in_word]:
            return existing
        else:
            return lst_candidate
