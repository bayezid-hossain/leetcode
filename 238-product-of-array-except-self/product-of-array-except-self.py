class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ansFor0=1
        zeroCount=0
        zeroIndex=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeroCount+=1
                zeroIndex=i
                
            else:
                ansFor0*=nums[i]
            
        result=[0] * len(nums)
        if zeroCount>1:
            return result
        elif zeroCount>0:
            result[zeroIndex]=ansFor0
        else:
            for i in range(len(nums)):
                result[i]=ansFor0//nums[i]
                
        return result