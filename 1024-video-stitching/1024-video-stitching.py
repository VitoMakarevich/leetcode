class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if time == 0: 
          return 0
        clips = sorted([(x, y) for idx, (x, y) in enumerate(clips)], key = lambda x: (x[0], -x[1]))
        if clips[0][0] > 0 or (len(clips) == 1 and clips[0][1] < time):
          return -1
        ans = 1
        picked_y = clips[0][1]
        idx = 1
        while picked_y < time:
          next_y = picked_y
          while idx < len(clips) and clips[idx][0] <= picked_y:
            next_y = max(clips[idx][1], next_y)
            idx += 1
          if next_y == picked_y:
            return -1
          picked_y = next_y
          ans += 1

        return ans