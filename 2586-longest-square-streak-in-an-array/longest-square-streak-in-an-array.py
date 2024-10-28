class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        sn=sorted(nums)
        counter={}
        for i in sn:
            counter[pow(i,2)]=counter.get(i,0)+1
     
        max_key = max(counter, key=counter.get)
        max_key=counter.get(max_key)
        return -1 if max_key==1 else max_key