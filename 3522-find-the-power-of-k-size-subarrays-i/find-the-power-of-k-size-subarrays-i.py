class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def getMax(start,end,nums):
            max_num=nums[start]
            for start in range(start+1,end):
                # print(nums[start])
                if max_num>=nums[start] or nums[start]-max_num!=1:
                    return -1
                else: max_num=nums[start]
            return max_num
        result=[]
        for i in range(0,len(nums)-k+1):
            # print(i)
            result.append(getMax(i,i+k,nums))
        return result