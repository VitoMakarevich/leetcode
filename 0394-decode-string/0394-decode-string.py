class Solution:
    def decodeString(self, s: str) -> str:
        multipliers = deque()
        strs = deque()
        i = 0
        number_local = deque()
        str_local = deque()
        numbers = set([str(i) for i in range(0, 10)])
        quotes = {'[', ']'}
        res = ""

        for cur in s:
            if cur in numbers:
                if len(str_local) > 0:
                    new_str = ''.join(str_local)
                    if len(multipliers) > 0:
                        new_s = new_str
                        while len(strs) >= len(multipliers):
                            new_symbol = strs.pop()
                            if new_symbol != '[':
                                new_s = f'{new_symbol}{new_s}'
                            else:
                                break
                        strs.append(new_s)
                    else:
                        res += new_str
                    str_local = deque()
                number_local.append(cur)
            elif cur == '[':
                multipliers.append(int(''.join(number_local)))
                number_local = deque()
                strs.append('[')
            elif cur == ']':
                multipler = multipliers.pop()
                prev = ''
                while len(strs) > len(multipliers):
                    new_symbol = strs.pop()
                    if new_symbol != '[':
                        prev = f"{new_symbol}{prev}"
                    else:
                        break
                new_str = (prev + ''.join(str_local)) * multipler
                if len(multipliers) == 0:
                    res += new_str
                else:
                    strs.append(new_str)
                str_local = deque()
            else:
                str_local.append(cur)
                
        return res + ''.join(str_local)
            
