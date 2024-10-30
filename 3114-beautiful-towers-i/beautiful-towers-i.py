class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        ans=0
        n=len(heights)

        for i in range(n):
            h=[0]*n
            h[i]=heights[i]

            for j in range(i-1,-1,-1):
                h[j]=min(heights[j],h[j+1])
            for j in range(i+1,n):
                h[j]=min(heights[j],h[j-1])
            
            ans=max(ans,sum(h))
        return ans
        