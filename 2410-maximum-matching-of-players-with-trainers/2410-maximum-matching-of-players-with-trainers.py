class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0
        players.sort(reverse = True)
        trainers.sort(reverse = True)
        p_ptr = 0
        for t_ptr in range(len(trainers)):
          while p_ptr < len(players) and trainers[t_ptr] < players[p_ptr]:
            p_ptr += 1
          if p_ptr != len(players):
            res += 1
            p_ptr += 1
          else:
            break
        return res