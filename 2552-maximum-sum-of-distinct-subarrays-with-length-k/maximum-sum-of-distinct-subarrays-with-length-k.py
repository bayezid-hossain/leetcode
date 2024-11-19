class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        ws = 0
        max_sum = 0

        for i in range(n):
            # Add the current element to the window
            mp[nums[i]] += 1
            ws += nums[i]

            # If the window size exceeds 'k', slide the window
            if i >= k:
                le = nums[i - k]
                mp[le] -= 1
                ws -= le
                if mp[le] == 0:
                    del mp[le]

            # Check if the window has exactly 'k' distinct elements
            if i >= k - 1 and len(mp) == k:
                max_sum = max(max_sum, ws)

        return max_sum

# class Solution:
#     def maximumSubarraySum(self, nums: List[int], k: int) -> int:
#         # max_sum=0
#         # subarr=set({})
#         # queue=[]
#         # left=0
#         # n=len(nums)
#         # right=k-1
#         # for i in range(k):
#         #     queue.append(nums[i])
#         # subarr.update(queue)
#         # # print(subarr)
#         # while right<n-1:
#         #     # print(queue)
#         #     if len(subarr)==k:
                
#         #         max_sum=max(max_sum,sum(subarr))
            
#         #     queue.pop(0)
#         #     queue.append(nums[right+1])
#         #     # print(queue)
#         #     subarr=set(queue)
#         #     left+=1
#         #     right+=1 
#         # queue.append(nums[right])
#         #     # print(queue)
#         # subarr=set(queue)
#         # print(subarr)
#         # if len(subarr)==k:

#         #     max_sum=max(max_sum,sum(subarr))
            
#         # return max_sum
        