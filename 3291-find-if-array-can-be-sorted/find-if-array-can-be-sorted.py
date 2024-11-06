class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
    
        def countSetBits(num)->int:
            total=0
            while num:
                total+=num&1
                num>>=1
            return total
        for _ in range(len(nums)):
            for i in range(len(nums)-1):
                if countSetBits(nums[i])==countSetBits(nums[i+1]) and nums[i+1]<nums[i]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
        
        return nums==sorted(nums)
            
            