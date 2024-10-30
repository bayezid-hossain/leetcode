class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)

        lis=[1]*n        
        #Calculating LIS
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    lis[i]=max(lis[i],lis[j]+1)

    
        #Calculating LDS
        lds=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if nums[i]>nums[j]:
                    lds[i]=max(lds[i],lds[j]+1)

        max_mountain=0
        for i in range(1,n-1):
            if lis[i]>1 and lds[i]>1: #valid peak
                max_mountain=max(max_mountain,lis[i]+lds[i]-1)

        return n-max_mountain

# Intuition
# To solve this problem, let’s think about what makes a mountain array:

# The array has to increase to a peak and then decrease.
# A mountain array has a single peak, meaning the sequence first strictly increases, reaches a peak, and then strictly decreases.
# With this in mind, the problem becomes finding the longest subarray that can form a mountain shape and then determining the minimum number of removals required to create it. We’ll use two sequences:

# Longest Increasing Subsequence (LIS) up to each point to form the "up" side.
# Longest Decreasing Subsequence (LDS) from each point to form the "down" side.
# Approach
# Calculate LIS and LDS:

# LIS: For each element, find the length of the longest increasing subsequence up to that element.
# LDS: For each element, find the length of the longest decreasing subsequence from that element.
# Find Maximum Mountain Length:

# For each potential peak (where both LIS[i] > 1 and LDS[i] > 1), calculate the mountain length as LIS[i] + LDS[i] - 1.
# Track the maximum mountain length we can form.
# Calculate Minimum Removals:

# Subtract the maximum mountain length from the total number of elements to get the minimum removals needed.
# Complexity
# Time Complexity: (O(n^2)), due to the LIS and LDS calculations for each element.
# Space Complexity: (O(n)), for storing the LIS and LDS arrays.

        