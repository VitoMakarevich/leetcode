class Solution:
    def partitionString(self, s: str) -> int:
        new = s
        counter = 0
        while len(new) > 0:
            i = 0
            current_s = set()
            while i < len(new) and new[i] not in current_s:
                current_s.add(new[i])
                i += 1
            if i == len(new):
                new = ''
            else:
                j = i
                current_s = set()
                while j < len(new) and new[i] not in current_s:
                    current_s.add(new[j])
                    j += 1
                if j - i > i:
                    if j != len(new):
                        new = new[0:i] + new[j:]
                    else:
                        new = new[0:i]
                else:
                    new = new[i:]
            counter += 1
        
        return counter
        
