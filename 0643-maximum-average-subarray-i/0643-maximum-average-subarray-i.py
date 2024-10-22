class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average=0
        newMax= float('-inf')

        leftWindow=0
        rightWindow=leftWindow+k-1
        for i in range(rightWindow+1):
            average+=nums[i]
        newMax=max(newMax,average)
        leftWindow+=1
        rightWindow+=1
        # print(newMax)
        while rightWindow<len(nums):
            average-=nums[leftWindow-1]
            average+=nums[rightWindow]
            newMax=max(newMax,average)
            leftWindow+=1
            rightWindow+=1
        
        # print(newMax)
        return newMax/k
            

