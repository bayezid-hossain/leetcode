class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        arr=[0]*25
        for i in candidates:
            br=bin(i)[2:].zfill(24)
            # print(br)

            for j in range(len(br)-1,-1,-1):
                if br[j]=="1":
                    arr[j]+=1
        
        max=0
        # print(arr)
        for i in range(len(arr)):
            if arr[i]>max:
                max=arr[i]
        return max