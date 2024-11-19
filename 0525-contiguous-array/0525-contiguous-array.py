class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = []
        for value in nums:
            if len(prefix_sum) == 0:
                prefix_sum.append(value if value == 1 else -1)
            else:
                v = value if value == 1 else -1
                prefix_sum.append(prefix_sum[-1] + v)
        counter = {0: [-1]}
        for k, v in enumerate(prefix_sum):
            cur_v = counter.get(v, [])
            cur_v.append(k)
            counter[v] = cur_v
        res = 0
        for values in counter.values():
            if len(values) > 1:
                res = max(res, values[-1] - values[0])
        return res

