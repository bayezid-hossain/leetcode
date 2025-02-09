class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n=len(nums)
        prefixArr=[0] * n

        for i in range(1,n):
            prefixArr[i]=prefixArr[i-1]

            if nums[i]%2==nums[i-1]%2:
                prefixArr[i]+=1
                
        result=[]
        for left,right in queries:
            special_count=prefixArr[right]-(prefixArr[left] if left>0 else 0)
            result.append(special_count==0)
        return result