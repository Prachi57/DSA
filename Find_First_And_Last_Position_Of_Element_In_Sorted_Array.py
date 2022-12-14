class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        n=len(nums)
        start,end=-1,-1
        l,r=0,n
        while(l<r):
            mid=(l+r)//2
            if nums[mid]>=target:
                r=mid
            else:
                l=mid+1
        if l<n and nums[l]==target:
            start=l
        l,r=0,n
        while(l<r):
            mid=(l+r)//2
            if(nums[mid]<=target):
                l=mid+1
            else:
                r=mid
        if nums[r-1]==target:
            end=r-1
        return [start,end]                       
            
     