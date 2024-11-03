class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest=float('inf')
        result=0
        nums=sorted(nums)
        for i in range(len(nums)-2):
            hi=len(nums)-1
            lo=i+1
            while lo<hi:
                sum=nums[i]+nums[lo]+nums[hi]
                if sum==target:
                    return sum
                diff=abs(sum-target)
                if diff<closest:
                    closest=diff
                    result=sum
                lo+=sum<target
                hi-=sum>target
        return result
