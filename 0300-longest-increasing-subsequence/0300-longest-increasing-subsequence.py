class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [{} for _ in range(len(nums))]
        cache[0] = {nums[0]: 1}
        for index, value in enumerate(nums[1:], start = 1):
            max_count = float('-inf')
            cache[index][value] = 1
            for prev_max, count in (cache[index - 1]).items():
                cache[index][prev_max] = count
                if prev_max < value and count > max_count:
                    max_count = count

            # print(f"index={index}, cur={value}, max_count={max_count}")

            if max_count != float('-inf'):
                cache[index][value] = max(1 + max_count, cache[index - 1].get(value, 1))
            
                

        # print(cache)
        return max(cache[len(nums)- 1].values())