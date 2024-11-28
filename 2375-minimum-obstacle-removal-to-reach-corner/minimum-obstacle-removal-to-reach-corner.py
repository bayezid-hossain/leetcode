class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        if n==1 and m==1:
            return grid[0][0]
        g = [[] for i in range(m * n)]
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(n):
            for j in range(m):
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        if grid[nx][ny]==1:
                            g[i*m + j].append([nx*m + ny, 1])
                        else:
                            # print(i,j,i*m + j , len(g))
                            g[i*m + j].append([nx*m + ny, 0])
        heap = [[grid[0][0], 0] ]
        n = len(g)
        dist = [float('inf')]*n
        dist[0] = grid[0][0] 
        # print(g[3])
        while heap:
            # print(heap)
            d,node = heappop(heap)
            if dist[node]<d:
                continue 
            for child,w in g[node]:
                # print(node,child, dist[child],d,w)
                if dist[child]>d +w:
                    dist[child] = d + w 
                    heappush(heap , [dist[child] , child])
        # print(dist)
        return dist[-1]