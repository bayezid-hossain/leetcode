class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap=[]
        for n in gifts:
            heapq.heappush(maxheap,-n)
            
        
        for i in range(k):
            maxnum=-heapq.heappop(maxheap)
            newnum=floor(pow(maxnum,0.5))
            heapq.heappush(maxheap,-newnum)
        return -(sum(maxheap))