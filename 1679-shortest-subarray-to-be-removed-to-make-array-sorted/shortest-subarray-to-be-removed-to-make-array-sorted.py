class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)

        left=0
        while left+1<n and arr[left]<=arr[left+1]:
            left+=1
        right=n-1
        if left==n-1:
            return 0
        while right>0 and arr[right-1]<=arr[right]:
            right-=1
            
        result=min(n-left-1,right)
        
        i,j=0,right
        while i<=left and j<n:
            if arr[i]<=arr[j]:
                result=min(result,j-i-1)
                i+=1
            else:
                j+=1
        return result


#         Intuition
# When I first saw this problem, I noticed that the goal is to make the array sorted by removing the shortest possible subarray. This means:

# We should look for any parts of the array that are already sorted and try to retain as much of that as possible.
# If we have a long sorted prefix (from the start) and a long sorted suffix (from the end), we might only need to remove a small subarray in between to make the entire array sorted.
# By focusing on these already sorted sections, we can potentially minimize the length of the subarray that needs to be removed.

# Approach
# Here’s the approach I used to solve this problem efficiently:

# Find the longest non-decreasing prefix from the beginning of the array. Let's call this left. This gives us the starting part of the array that’s already sorted.

# Find the longest non-decreasing suffix from the end of the array. Let's call this right. This gives us the ending part of the array that’s already sorted.

# Check if the entire array is sorted by verifying if left spans the whole array. If so, the answer is 0 because we don't need to remove anything.

# Calculate minimum removal:

# Initially, consider removing either the entire suffix (n - left - 1 elements) or the entire prefix (right elements).
# Use a two-pointer technique to see if we can merge parts of the prefix and suffix by skipping the smallest possible middle section. This allows us to explore shorter subarrays to remove.
# Return the result which is the minimum number of elements we need to remove.