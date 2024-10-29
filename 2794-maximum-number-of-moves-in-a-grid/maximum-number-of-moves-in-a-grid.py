class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        
        memo={}
        
        def dfs(row,col):
            nonlocal memo
            # return if already calculated length for current row and col
            if (row,col) in memo:
                return memo[(row,col)]
            moves=0
            
            # check 3 possible places for next dfs, upper right cell, right cell, bottom right cell, if any or all of these cells are strictly greater than current cell then we do dfs again, so we store moves as the max of 1+dfs of next cell
            for r,c in [(row-1,col+1),(row,col+1),(row+1,col+1)]:
                if 0<=r<rows and 0<=c<cols and grid[r][c]>grid[row][col]:
                    moves=max(moves,1+dfs(r,c))
            
            #store result in memo
            memo[(row,col)]=moves
            return moves
        
        max_moves=0
        #check max moves for each row
        for row in range(rows):
            max_moves=max(max_moves,dfs(row,0))
        return max_moves
