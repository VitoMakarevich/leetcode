class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        l,u = len(nums)-1, 0
        stck=[]
        for i in range(len(nums)):
            while stck and nums[stck[-1]]>nums[i]:
                l = min(l, stck.pop())
            stck.append(i)
        
        stck=[]        
        for i in range(len(nums)-1,-1, -1):
            while stck and nums[stck[-1]]<nums[i]:
                u = max(u, stck.pop())
            stck.append(i)
        
        return 0 if l>=u else u-l+1