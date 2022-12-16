class Solution(object):
    def search(self, nums, target):
        s=0
        e=len(nums)-1
        while(s<=e):
            mid=(s+e)//2
            if nums[mid]==target:
                return mid
            elif s==mid==e:
                return -1    
            elif nums[s]<=nums[mid]:
                if nums[s]<=target<=nums[mid]:
                    e=mid
                else:
                    s=mid+1
            else:
                if nums[mid]<target<nums[s]:
                    s=mid+1
                else:
                    e=mid
        return -1          