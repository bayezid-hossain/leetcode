class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        range_max=float('-inf')
        range_min=float('inf')
        left=0
        win_size=0
        count=0
        
        
        for right in range(n):
            range_max=max(range_max,nums[right])
            range_min=min(range_min,nums[right])
            
            if range_max-range_min>2:
                win_size=right-left
                
                # print(win_size)
                count+=((win_size*(win_size+1))//2)
                # print(count)
                left=right
                range_min=nums[right]
                range_max=nums[right]
                
                while abs(nums[right]-nums[left-1])<=2:
                    left-=1
                    range_max=max(range_max,nums[left])
                    range_min=min(range_min,nums[left])
                
                if left<right:
                    win_size=right-left
                    # print(win_size)
                    count-=((win_size*(win_size+1))//2)
                    # print(count)
                    
        
        win_size=right-left+1
        # print(win_size)
        count+=((win_size*(win_size+1))//2)
        # print(count)
        return count        