class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def isPossible(x, quantities,n):
            sum=0
            for i in quantities:
                sum+=ceil(i/x)
            return sum>n
        

        left=1
        right=max(quantities)
        while left<right:
            mid=(right+left)//2
            if isPossible(mid,quantities,n):
                left=mid+1
            else:
                right=mid
        return left
