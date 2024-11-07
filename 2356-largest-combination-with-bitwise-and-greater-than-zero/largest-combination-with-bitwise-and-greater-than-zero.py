class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        mask=1
        max=0
        for shift in range(24):
            count=0
            for num in candidates:
                if num & mask:
                    count+=1
            if count>max:
                max=count
            mask<<=1
        return max