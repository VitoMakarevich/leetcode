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
                            new_s = f'{strs.pop()}{new_s}'
                        strs.append(new_s)
                    else:
                        # print(f"appending in {cur}")
                        res += new_str
                    str_local = deque()
                number_local.append(cur)
            elif cur == '[':
                multipliers.append(int(''.join(number_local)))
                number_local = deque()
            elif cur == ']':
                # print(f"multiplers={multipliers}, str_local={str_local} strs={strs}, res={res}")
                multipler = multipliers.pop()
                prev = ''
                while len(strs) > len(multipliers):
                    prev = f"{strs.pop()}{prev}"
                new_str = (prev + ''.join(str_local)) * multipler
                # print(new_str)
                if len(multipliers) == 0:
                    # print(f"miltipliers = {multipliers}")
                    res += new_str
                else:
                    strs.append(new_str)
                str_local = deque()
            else:
                str_local.append(cur)
                
        return res + ''.join(str_local)
            
