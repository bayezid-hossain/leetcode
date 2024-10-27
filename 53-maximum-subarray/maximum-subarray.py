class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-INF')
        sum=0
        
        for i in nums:
            sum+=i
            if sum>max_sum:
                max_sum=sum
            if sum<0:
                sum=0
        
        return max_sum