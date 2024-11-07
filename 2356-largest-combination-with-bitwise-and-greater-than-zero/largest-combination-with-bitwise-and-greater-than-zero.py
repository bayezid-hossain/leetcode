class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        arr=[0]*25
        max=0
        for i in candidates:
            br=bin(i)[2:].zfill(24)
            # print(br)

            for j in range(len(br)-1,-1,-1):
                if br[j]=="1":
                    arr[j]+=1
                    max=arr[j] if arr[j]>max else max
        return max