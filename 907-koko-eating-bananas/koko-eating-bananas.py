class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(x,piles,h):
            sum=0
            for i in piles:
                sum+=ceil(i/x)
            return sum>h
        
        left=1
        right=max(piles)
        while left<right:
            mid=(left+right)//2
            
            if isPossible(mid,piles,h):
                left=mid+1
            else:
                right=mid
        return left