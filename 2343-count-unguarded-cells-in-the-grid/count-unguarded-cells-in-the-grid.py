class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]* n for i in range(m)]
        count=0
        for r,c in guards:
            grid[r][c]=1
            count+=1
        for r,c in walls:
            grid[r][c]=1
            count+=1
        # print(grid)

        directions=[(-1,0),(1,0),(0,1),(0,-1)]
       
        for r,c in guards:
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                while 0<=nr<m and 0<=nc<n:
                    if grid[nr][nc]==1:
                        break
                    if grid[nr][nc]==0:
                        grid[nr][nc]=2

                        count+=1
                    nr+=dr
                    nc+=dc
        return (m*n)-count
       #TLE
        # grid=[[0] * n] *m
        
        
        # wal_map=set({})
        # marked_cell=set({})
        # for wall in walls:
        #     # print(wall)
        #     wal_map.add((wall[0],wall[1]))
        #     marked_cell.add((wall[0],wall[1]))
        # # print(wal_map)
        # for guard in guards:
        #     #traverse left
        #     row,col=guard
        #     while col >=0 and (row,col) not in wal_map:
        #         marked_cell.add((row,col))
        #         col-=1
                
        #     #traverse right
        #     row,col=guard
        #     while col<n and (row,col) not in wal_map:
        #         marked_cell.add((row,col))
        #         col+=1
                
        #     #traverse top
        #     row,col=guard
        #     while row>=0 and (row,col) not in wal_map:
        #         marked_cell.add((row,col))
        #         row-=1  
                
        #     #traverse down
        #     row,col=guard
        #     while row<m and (row,col) not in wal_map:
        #         marked_cell.add((row,col))
        #         row+=1
                
        # return ((m*n)-len(marked_cell))