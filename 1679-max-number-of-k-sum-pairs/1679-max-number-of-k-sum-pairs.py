class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        left=0
        count=0
        right=len(nums)-1
        while left<right:
            result=nums[left]+nums[right]
            if result==k:
                count+=1
                left+=1
                right-=1
            elif result<k:
                left+=1
            elif result>k:
                right-=1
        return count