class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts=[-x for x in gifts]
        
        heapify(gifts)
        
        for i in range(k):
            maxnum=-heapq.heappop(gifts)
            newnum=floor(pow(maxnum,0.5))
            heapq.heappush(gifts,-newnum)
        return -(sum(gifts))