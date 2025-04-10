class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
      if not nums:
        return 0
      min_v, max_v = min(nums), max(nums)
      segment_tree = SegmentTree(min_v, max_v)
      min_so_far = nums[0]
      for v in nums: 
        length_smaller, count_smaller = segment_tree.query(min_so_far, v - 1)
        segment_tree.update(v, (length_smaller + 1, count_smaller))
        min_so_far = min(v, min_so_far)
      return segment_tree.query(min_v, max_v)[1]
        

class SegmentNode:
  # length 0, count 1
  DEFAULT = (0, 1)
  def __init__(self, start, end, value=DEFAULT, left=None, right=None):
    self.start = start
    self.end = end
    self.mid = (self.start + self.end) // 2
    self.value = value
    self.left = left
    self.right = right
  def safe_left(self):
    self.left = self.left if self.left else SegmentNode(self.start, self.mid)
    return self.left
  def safe_right(self):
    self.right = self.right if self.right else SegmentNode(self.mid + 1, self.end)
    return self.right

def merge_segments(s1: Tuple[int, int], s2:Tuple[int, int]) -> Tuple[int, int]:
  length_s1, count_s1 = s1
  length_s2, count_s2 = s2
  if length_s1 != 0 and length_s1 == length_s2:
    return (length_s1, count_s1 + count_s2)
  return max(s1, s2)
  

class SegmentTree:
  def __init__(self, min_v: int, max_v: int) -> None:
    self.root = SegmentNode(min_v, max_v)
  
  def _update(self, node: SegmentNode, number: int, value: Tuple[int, int]):
    if node.start == node.end:
      node.value = merge_segments(node.value, value)
      return
    if node.mid < number:
      self._update(node.safe_right(), number, value)
    else:
      self._update(node.safe_left(), number, value)
    node.value = merge_segments(node.safe_left().value, node.safe_right().value)
  
  def update(self, number: int, value: Tuple[int, int]) -> None:
    self._update(self.root, number, value)

  def _query(self, node: SegmentNode, start: int, end: int) -> Tuple[int, int]:
    if end < node.start or start > node.end:
      return SegmentNode.DEFAULT
    if start <= node.start and end >= node.end:
      return node.value
    return merge_segments(self._query(node.safe_left(), start, end), self._query(node.safe_right(), start, end))

  def query(self, start: int, end: int) -> Tuple[int, int]:
    return self._query(self.root, start, end)
