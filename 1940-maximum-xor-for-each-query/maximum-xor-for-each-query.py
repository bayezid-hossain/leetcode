class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxPossible=pow(2,maximumBit)-1
        prexor=[nums[0]]
        result=[prexor[0]^maxPossible]
        
        for i in range(1,len(nums),1):
            prexor.append(prexor[i-1]^nums[i])
            result.append(maxPossible^prexor[i])
        return result[::-1]


        