class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        m,n=len(robot),len(factory)
        dp=[[0]*(n+1) for _ in range((m+1))]
        
        
        for i in range(m):
            dp[i][-1]=float('inf')
        
        for i in range(n-1,-1,-1):
            prefix=0
            qq=deque([(m,0)])
            
            for j in range(m-1,-1,-1):
                prefix+=abs(robot[j]-factory[i][0])
                
                if qq[0][0]>j+factory[i][1]:
                    qq.popleft()
                    
                while qq and qq[-1][1]>=dp[j][i+1]-prefix:
                    qq.pop()
                
                qq.append((j,dp[j][i+1]-prefix))
                dp[j][i]=qq[0][1]+prefix
        return dp[0][0]
        
         # Sort positions to enable optimal matching
            
#         # DP table initialization
#         dp = [[0]*(n+1) for _ in range(m+1)]
        
#         # Base case: if no factories left, distance is infinite
#         for i in range(m): 
#             dp[i][-1] = float('inf')
        
#         # Process each factory from right to left
#         for j in range(n-1, -1, -1):
#             prefix = 0
#             qq = deque([(m, 0)])
            
#             # Process each robot from right to left
#             for i in range(m-1, -1, -1):
#                 # Add distance to current factory
#                 prefix += abs(robot[i] - factory[j][0])
                
#                 # Remove elements outside factory limit window
#                 if qq[0][0] > i+factory[j][1]: 
#                     qq.popleft()
                
#                 # Maintain monotonic queue property
#                 while qq and qq[-1][1] >= dp[i][j+1] - prefix:
#                     qq.pop()
                    
#                 qq.append((i, dp[i][j+1] - prefix))
#                 dp[i][j] = qq[0][1] + prefix
                
#         return dp[0][0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      