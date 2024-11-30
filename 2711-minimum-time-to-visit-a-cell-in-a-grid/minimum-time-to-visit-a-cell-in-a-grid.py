class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        m,n=len(grid),len(grid[0])
        heap=[(0,0,0)]
        visited=set()

        while heap:
            time,r,c=heapq.heappop(heap)
            
            if (r,c)==(m-1,n-1):
                return time
            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            
            for nr,nc in nei:
                
                if nr<0 or nc<0 or nr==m or nc==n or (nr,nc) in visited:
                    continue
                wait=0
                
                if abs(grid[nr][nc]-time)%2==0:
                    wait+=1
                n_time=max(grid[nr][nc]+wait,time+1)
                heapq.heappush(heap,(n_time,nr,nc))
                
                visited.add((nr,nc))