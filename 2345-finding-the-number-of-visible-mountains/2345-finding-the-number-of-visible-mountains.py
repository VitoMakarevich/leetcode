class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        queue = deque()
        peaks.sort(key = lambda x: x[0])
        for item in peaks:
          item_tuple = (item[0], item[1])
          # if something in queue and cur is not overlapped by last
          if len(queue) == 0 or not self.does_left_overlap_right_right_side(queue[-1], item_tuple):
            # while last overlaps some previous - delete those
            while len(queue) >= 1 and self.does_left_overlap_right_left_side(item_tuple, queue[-1]):
              queue.pop()
            queue.append(item_tuple)
        
        # print(queue)
        counter = Counter(queue)
        return sum(1 for x in counter.values() if x == 1)
    def does_left_overlap_right_right_side(self, left, right):
        res = left[1] > right[1] and left[1] + left[0] >= right[0] + right[1]
        # print(f"for left={left}, right={right}, left_overlap res={res}")
        return res

    def does_left_overlap_right_left_side(self, left, right):
        res = left[1] > right[1] and left[0] - left[1] <= right[0] - right[1]
        # print(f"for left={left}, right={right}, right_overlap res={res}, l_diff = {left[1] - left[0]}, r_diff = {right[0] - right[1]}")
        return res