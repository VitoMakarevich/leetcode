EMPTY_LIST = []
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        routes_by_stop = {}
        if source == target:
          return 0
        for index, route in enumerate(routes):
          for stop in route:
            existing_routes = routes_by_stop.get(stop, set())
            existing_routes.add(index)
            routes_by_stop[stop] = existing_routes

        if not target in routes_by_stop or not source in routes_by_stop:
          return -1
        q = deque([source])
        routes_visited = set()
        stops_visited = set()
        switches = 1
        while len(q):
          for _ in range(len(q)):
            stop = q.popleft()
            routes_in_this_stop = routes_by_stop.get(stop, EMPTY_LIST)
            for next_route in routes_in_this_stop:

              if next_route in routes_visited:
                continue

              routes_visited.add(next_route)

              for next_stop in routes[next_route]:
                if next_stop in stops_visited:
                  continue
                if next_stop == target:
                  return switches
                stops_visited.add(next_stop)
                q.append(next_stop)
          switches += 1
        
        return -1
