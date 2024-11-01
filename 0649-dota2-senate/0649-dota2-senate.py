class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        voted = deque()
        not_voted = deque()
        for vote in senate:
            if not_voted and not_voted[-1] != vote:

                voted.append(not_voted.pop())
            else:
                not_voted.append(vote)
         
        new_iter_set = set(voted + not_voted)
        iterations = not_voted + voted
        while len(new_iter_set) != 1:
            voted = deque()
            not_voted = deque()
            for vote in iterations:
                if not_voted and not_voted[-1] != vote:
                    voted.append(not_voted.pop())
                else:
                    not_voted.append(vote)
            iterations = not_voted + voted
            new_iter_set = set(voted + not_voted)
        
        return self.fmt(next(iter(new_iter_set)))
            
    def fmt(self, v):
        if v == 'R':
            return 'Radiant'
        else:
            return 'Dire'