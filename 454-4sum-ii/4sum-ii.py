class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic={}
        for i in nums1:
            for j in nums2:
                res=i+j
                
                if res in dic:
                    dic[res]+=1
                else: dic[res]=1
        count=0
        for i in nums3:
            for j in nums4:
                target=0-(i+j)
                
                if target in dic:
                    count+=dic[target]
        return count