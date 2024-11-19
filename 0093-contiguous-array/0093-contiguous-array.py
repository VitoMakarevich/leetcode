class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = []
        for value in nums:
            prev = 0 if len(prefix_sum) == 0 else prefix_sum[-1]
            
            v = value if value == 1 else -1
            prefix_sum.append(prev + v)
        counter = {0: [-1]}
        for k, v in enumerate(prefix_sum):
            cur_v = counter.get(v, [])
            if len(cur_v) == 0 or len(cur_v) == 1:
                cur_v.append(k)
            else:
                cur_v[1] = k
            counter[v] = cur_v
        res = 0
        for values in counter.values():
            if len(values) > 1:
                res = max(res, values[1] - values[0])
        return res

