class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        queue=deque()
        rows = len(grid)
        cols = len(grid[0])
        # first scan to find the treasure
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append((r,c,0))
        
        while(queue):
            r,c,dist = queue.popleft()

            # check 4 neighs
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                rw = r+dr
                cw = c+dc
                if rw<0 or rw>=rows or cw<0 or cw>=cols:
                    continue
                if grid[rw][cw]==2147483647:
                    grid[rw][cw]=dist+1
                    queue.append((rw,cw, dist+1))
    



