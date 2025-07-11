class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        events = [(0, 0)] + list(zip(startTime, endTime)) + [(eventTime, eventTime)]
        gaps = [s2 - e1 for (s1, e1), (s2, e2) in pairwise(events)]
        max_gap_to_right = [0] * (len(gaps))
        for gap_index in range(len(gaps) - 2, -1, -1):
          max_gap_to_right[gap_index] = max(gaps[gap_index + 1], max_gap_to_right[gap_index + 1])
        max_gap_to_left = [0] * (len(gaps))
        for idx in range(1, len(gaps)):
          max_gap_to_left[idx] = max(max_gap_to_left[idx - 1], gaps[idx - 1])
        res = 0
        for event_idx in range(len(startTime)):
          gap_to_left = gaps[event_idx]
          gap_to_right = gaps[event_idx + 1]
          start, end = events[event_idx + 1]
          event_duration = end - start
          res_if_move_to_end = gap_to_right + gap_to_left
          res_if_change_pos = gap_to_right + gap_to_left + event_duration if max_gap_to_left[event_idx] >= event_duration or max_gap_to_right[event_idx + 1] >= event_duration else 0
          res = max(res, res_if_move_to_end, res_if_change_pos)

        return res
