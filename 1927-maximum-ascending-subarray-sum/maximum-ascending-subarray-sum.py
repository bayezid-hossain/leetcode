class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxNum=0
        sumNum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                maxNum=max(maxNum,sumNum)
                sumNum=nums[i]
            else:
                sumNum+=nums[i]
        return max(maxNum,sumNum)