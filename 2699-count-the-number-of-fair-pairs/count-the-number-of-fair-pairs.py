class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        count=0
        #bruteforce TLE
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums),1):
        #         # print(i,j)
        #         if lower<=nums[i]+nums[j]<=upper:
        #             count+=1

        nums.sort()
        n=len(nums)
        for i in range(n-1):
            min_val=lower-nums[i]
            max_val=upper-nums[i]

            start=bisect_left(nums,min_val,i+1)
            end=bisect_right(nums,max_val,i+1)
            count+=end-start
        
        return count