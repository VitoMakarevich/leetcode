class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        queue = deque()
        idx_to_max = {}
        for index in range(len(nums2)):
          while queue and nums2[index] > nums2[queue[-1]]:
            prev = queue.pop()
            idx_to_max[nums2[prev]] = nums2[index]
          queue.append(index)
        for index in queue:
          idx_to_max[nums2[index]] = -1
        
        res = [idx_to_max[v] for v in nums1]
        return res
        