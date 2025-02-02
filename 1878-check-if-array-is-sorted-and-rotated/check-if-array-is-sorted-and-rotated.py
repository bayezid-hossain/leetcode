class Solution:
    def check(self, nums: List[int]) -> bool:

        n=len(nums)
        if n==1:
            return True
        firstNum=nums[0]

        index=1

        while index<n and nums[index]>=nums[index-1]:
            index+=1
        if index==n:
            return True
        # print(index)
        index+=1
        while index<n and nums[index]>=nums[index-1]:
            index+=1
        if index==n and nums[index-1]<=firstNum:
            return True
        return False