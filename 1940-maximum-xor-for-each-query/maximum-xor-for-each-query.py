class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prexor=[]
        prexor.append(nums[0])
        for i in range(1,len(nums),1):
            prexor.append(prexor[i-1]^nums[i])
        result=[]
        maxPossible=pow(2,maximumBit)-1
        # print(maxPossible)
        for i in range(len(prexor)):
            result.append(maxPossible^prexor[i])
        
        return result[::-1]


        