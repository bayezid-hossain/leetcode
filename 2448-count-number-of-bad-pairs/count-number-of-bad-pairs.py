class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        badpairs=0
        pairmap={}

        for pos in range(len(nums)):
            diff=pos-nums[pos]

            goodpairs=pairmap.get(diff,0)

            badpairs+=pos-goodpairs

            pairmap[diff]=goodpairs+1
        return badpairs