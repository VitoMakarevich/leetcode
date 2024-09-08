from collections import defaultdict, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_val = None
        min_len = float('inf')

        i = 0
        j = 0
        currently_used_map = defaultdict(int)
        required_dict = defaultdict(int)
        for w in t:
            required_dict[w] = required_dict.get(w, 0) + 1
        remaining_dict = required_dict.copy()
        queue = deque()
        while j < len(s):
            l = s[j]
            
            if l in required_dict:
                queue.append(l)
                currently_used_map[l] = currently_used_map.get(l, 0) + 1
                if remaining_dict.get(l, 0) > 0:
                    remaining_dict[l] = remaining_dict[l] - 1
                # print(i, j, remaining_dict)
                if sum(remaining_dict.values()) == 0:
                    while i <= j:
                        if s[i] not in required_dict:
                            i += 1
                            continue
                        first_element = queue.popleft()
                        # print(currently_used_map, queue)
                        currently_used_map[first_element] -= 1
                        if currently_used_map[first_element] < required_dict[first_element]:
                            # print(f"found exhaustion of {first_element} at len {i}-{j}, {currently_used_map}")
                            min_length = j - i
                            if min_length < min_len:
                                min_val = s[i: j + 1]
                                min_len = j + 1 - i
                            remaining_dict[first_element] += 1
                            i += 1
                            break
                        i += 1
            j += 1

        return "" if not min_val else min_val
            
