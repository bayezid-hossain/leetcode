class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        countNeg=0
        summation=0
        smallestAbs=float('inf')
        for r in range(row):
            for c in range(col):
                curAbs=abs(matrix[r][c])
                summation+=curAbs
                smallestAbs=min(smallestAbs,curAbs)
                if matrix[r][c]<0:
                    countNeg+=1
        
        if countNeg%2==0:
            return summation
        else:
            return summation-(2*smallestAbs)