class Solution(object):
    def singleNumber(self, nums):
        freq={}
        k=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq=1
        for a,b in freq.items():
            if(b==1):
                k.append(a)
        return k        
                