class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        visited=set()
        count_island=0

        def dfs(r,c):
            # base conditions
            # if out of bounds
            if r<0 or r>=rows or c<0 or c>=cols: return
            # if water found
            if grid[r][c]=="0": return
            # if already visited
            if (r,c) in visited: return

            #mark visited
            visited.add((r,c))

            #invoke nearby cells
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)

        # outer loop
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    # found a new island
                    count_island+=1
                    # look around using recursion
                    dfs(i,j)
        
        return count_island