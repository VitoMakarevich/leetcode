class Solution:
    def partitionString(self, s: str) -> int:
        new = s
        counter = 0
        i = 0
        left_set = set() 
        while len(new) > 0:   
            while i < len(new) and new[i] not in left_set:
                left_set.add(new[i])
                i += 1
            if i == len(new):
                new = ''
            else:
                if len(new) - i > i:
                    j = i
                    right_set = set()
                    while j < len(new) and new[i] not in right_set:
                        right_set.add(new[j])
                        j += 1
                    j_for_compare = j - int(j == len(new))
                    if j_for_compare - i > i:
                        if j != len(new):
                            new = new[0:i] + new[j:]
                        else:
                            new = new[0:i]
                    else:
                        new = new[i:]
                        i = 0
                        left_set = set()
                else:
                    new = new[i:]
                    i = 0
                    left_set = set()
            counter += 1
        
        return counter
        
