class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        arr=[0] *( n+1)
        
        for i in banned:
            if i<=n:
                arr[i]=1
                
        sum=0
        i=1
        count=0
        while sum<=maxSum and i<=n:
            if arr[i]!=1:
                sum+=i
                count+=1
            i+=1
        
        return count-1 if sum>maxSum else count
            