class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        countNeg=0
        summation=0
        smallestAbs=float('inf')
        for r in matrix:
            for c in r:
                
                if c<0:
                    c=-c
                    countNeg+=1
                summation+=c
                if c<smallestAbs:
                    smallestAbs=c
        
        if countNeg%2==0:
            return summation
        else:
            return summation-(2*smallestAbs)