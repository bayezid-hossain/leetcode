class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        length = len(nums)

        # Check all pairs of elements to see if the array can be sorted
        for i in range(length):
            for j in range(i + 1, length):
                # If elements are out of order
                if nums[j] < nums[i]:
                    # Check if they have the same bit count
                    if bin(nums[i]).count('1') != bin(nums[j]).count('1'):
                        # Return false if they can't be swapped to sort the array
                        return False

                    # Swap elements to move the smaller one forward
                    nums[i], nums[j] = nums[j], nums[i]

        # Final check to ensure the array is sorted
        for k in range(length - 1):
            if nums[k] > nums[k + 1]:
                return False

        return True
            
            