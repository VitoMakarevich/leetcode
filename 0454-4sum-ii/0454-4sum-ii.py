class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums4set = Counter(nums4)
        nums3set = Counter(nums3)
        nums3and4combs = {}
        for v3, c3 in nums3set.items():
            for v4, c4 in nums4set.items():
                s = v3 + v4
                nums3and4combs[s] = nums3and4combs.get(s, 0) + c4 * c3
        
        nums2set = Counter(nums2)
        nums1set = Counter(nums1)
        nums1and2combs = {}
        for v1, c1 in nums1set.items():
            for v2, c2 in nums2set.items():
                s = v1 + v2
                nums1and2combs[s] = nums1and2combs.get(s, 0) + c1 * c2
        
        res = 0
        for v12, c12 in nums1and2combs.items():
            target = 0 - v12
            if target in nums3and4combs:
                res += c12 * nums3and4combs[target]
        return res