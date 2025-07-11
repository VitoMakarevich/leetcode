from typing import List
from itertools import pairwise

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        events = [(0, 0)] + list(zip(startTime, endTime)) + [(eventTime, eventTime)]
        gaps = [s2 - e1 for (s1, e1), (s2, e2) in pairwise(events)]
        n = len(gaps)

        # Precompute max gaps to the right
        max_gap_to_right = [0] * n
        for i in range(n - 2, -1, -1):
            max_gap_to_right[i] = max(gaps[i + 1], max_gap_to_right[i + 1])

        # Precompute max gaps to the left
        max_gap_to_left = [0] * n
        for i in range(1, n):
            max_gap_to_left[i] = max(max_gap_to_left[i - 1], gaps[i - 1])

        res = 0
        for i in range(len(startTime)):
            start, end = events[i + 1]
            event_duration = end - start
            combined_gap = gaps[i] + gaps[i + 1]

            can_relocate = (
                max_gap_to_left[i] >= event_duration or
                max_gap_to_right[i + 1] >= event_duration
            )

            if can_relocate:
                res = max(res, combined_gap + event_duration)
            else:
                res = max(res, combined_gap)

        return res
