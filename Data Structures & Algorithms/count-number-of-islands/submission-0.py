class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        visited = set()

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            
            if (r,c) in visited: return
            if grid[r][c]=="0": return

            visited.add((r,c))

            # check its neighbours
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        count_island = 0
        # outerloop
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    count_island+=1
                    dfs(r,c)
        
        return count_island