class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res=float('inf')

        min_heap=[]
        cur_sum=0

        for r in range(len(nums)):
            cur_sum+=nums[r]

            if cur_sum>=k:
                res=min(res,r+1)

            while min_heap and cur_sum-min_heap[0][0]>=k:
                prefix_sum,end_idx=heapq.heappop(min_heap)
                res=min(res,r-end_idx)
            heapq.heappush(min_heap,(cur_sum,r))

        return -1 if res==float('inf') else res