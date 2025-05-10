class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pos_in_right = {}
        for index, value in enumerate(nums2):
          pos_in_right[value] = index
        res = []
        for v in nums1:
          out = -1
          for index in range(pos_in_right[v] + 1, len(nums2)):
            if nums2[index] > v:
              out = nums2[index]
              break
          res.append(out)
        return res