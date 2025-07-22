class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0
        players = [-p for p in players]
        heapq.heapify(players)
        trainers = [-t for t in trainers]
        heapq.heapify(trainers)
        while players and trainers:
          best_trainer = -trainers[0]
          best_player = -players[0]
          if best_trainer >= best_player:
            res += 1
            heapq.heappop(trainers)
            heapq.heappop(players)
          else:
            heapq.heappop(players)
            
        return res