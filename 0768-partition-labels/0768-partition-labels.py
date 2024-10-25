class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_pos = {}
        for i, c in enumerate(s):
            max_pos[c] = i
        
        split_pos = 0
        res = []
        for i, c in enumerate(s):
            if i > split_pos:
                prev_end = 0 if len(res) == 0 else sum(res)
                res.append(i - prev_end)
                split_pos = max_pos[c]
            else:
                split_pos = max(split_pos, max_pos[c])
            
        # print(split_pos)
        res.append(len(s) - sum(res))
            

        return res
        