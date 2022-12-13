class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        b=[]
        for i in range(len(nums)):
            if(nums[i]==target):
                b.append(i)
        return b       