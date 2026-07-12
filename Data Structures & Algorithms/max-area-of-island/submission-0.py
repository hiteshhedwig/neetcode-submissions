class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()

        def dfs(r,c):
            # check out of bounds
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            if (r,c) in visited:
                return 0
            if grid[r][c]==0: return 0

            visited.add((r,c))
            return 1 + dfs(r,c+1) + dfs(r,c-1) + dfs(r+1,c) + dfs(r-1,c)
            

        #outer loop
        max_area=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    max_area=max(dfs(i,j),max_area)
        
        return max_area

