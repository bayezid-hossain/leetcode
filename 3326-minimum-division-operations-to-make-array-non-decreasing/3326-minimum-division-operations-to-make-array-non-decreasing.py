class Solution:
    def minOperations(self, nums: List[int]) -> int:
        steps=0
        def largestDivisor(n1,n2):
            for i in range(2, n1 + 1):
                if n2 % i == 0: 
                    return i
            return -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>nums[i+1]:
                nums[i]=largestDivisor(nums[i+1],nums[i])
                if nums[i]==-1:
                    return -1
                steps+=1
        return steps

        
