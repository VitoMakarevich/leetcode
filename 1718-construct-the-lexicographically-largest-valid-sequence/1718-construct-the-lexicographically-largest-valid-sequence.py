from typing import List

placeholder = 0

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        target_len = 2 * n - 1
        used = [False] * (n + 1)
        cur = [placeholder] * target_len

        self.backtrack(used, n, cur, 0, target_len)
        return cur

    def backtrack(self, used, n, cur, idx, len_res):
        if idx == len_res:
            return True
        if cur[idx] != 0:
            return self.backtrack(used, n, cur, idx + 1, len_res)

        for number_to_put in range(n, 0, -1):
            if used[number_to_put]:
                continue

            if number_to_put == 1:
                cur[idx] = number_to_put
                used[number_to_put] = True
                if self.backtrack(used, n, cur, idx + 1, len_res):
                    return True
                cur[idx] = placeholder
                used[number_to_put] = False

            elif idx + number_to_put < len_res and cur[idx + number_to_put] == placeholder:
                cur[idx] = number_to_put
                cur[idx + number_to_put] = number_to_put
                used[number_to_put] = True
                if self.backtrack(used, n, cur, idx + 1, len_res):
                    return True
                cur[idx] = placeholder
                cur[idx + number_to_put] = placeholder
                used[number_to_put] = False

        return False
