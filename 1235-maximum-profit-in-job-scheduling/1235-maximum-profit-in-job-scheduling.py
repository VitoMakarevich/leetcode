class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self._intervals = []
        for start, end, profit in zip(startTime, endTime, profit):
            self._intervals.append((start, end, profit))
        self._intervals.sort()
        self._starts = [interval[0] for interval in self._intervals]

        return self._dp(0)

    @cache
    def _dp(self, i):
        if i == len(self._intervals):
            return 0
        next_possible_interval = self._next_interval(i + 1, self._intervals[i][1])
        print(f"for this interval {self._intervals[i]}, next is {next_possible_interval}, which is {0 if next_possible_interval == -1 else self._intervals[next_possible_interval]}")
        if next_possible_interval != -1:
            return max(self._intervals[i][2] + self._dp(next_possible_interval), self._dp(i + 1))
        else:
            return max(self._intervals[i][2], self._dp(i + 1))
    

    # target = 20
    # [1, 3, 5, 6, 8]
    @cache
    def _next_interval(self, start_i, target):
        low, high = start_i, len(self._starts) - 1
        while low < high:
            mid = (low + high) // 2
            if self._starts[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low if low < len(self._starts) and self._starts[low] >= target else -1

