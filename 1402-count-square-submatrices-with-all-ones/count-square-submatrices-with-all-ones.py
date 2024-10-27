class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Get dimensions of the matrix
        n=len(matrix)
        m=len(matrix[0])
        
        ans=0
        dp=[[0]*m for i in range(n)]
        for i in range(n):
            dp[i][0]=matrix[i][0]
            ans+=dp[i][0]
        for j in range(1, m):
            dp[0][j] = matrix[0][j]
            ans += dp[0][j]
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==1:
                    dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
                ans+=dp[i][j]
        # print(dp)
        return ans
    

        
#         # Fill the DP table for remaining cells
#         for i in range(1, n):
#             for j in range(1, m):
#                 # Only process if current cell in matrix is 1
#                 if matrix[i][j] == 1:
#                     # Find minimum of left, top, and diagonal cells and add 1
#                     dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
#                 ans += dp[i][j]
        
#         return ans