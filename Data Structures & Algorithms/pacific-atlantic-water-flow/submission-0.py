from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(grid, x, y, prev, ds):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                return

            if (y,x) in ds:
                return

            if grid[y][x] < prev:
                return

            ds.add((y,x))

            # recorrer todas las direcciones
            dfs(grid,x+1,y,grid[y][x],ds)
            dfs(grid,x-1,y,grid[y][x],ds)
            dfs(grid,x,y+1,grid[y][x],ds)
            dfs(grid,x,y-1,grid[y][x],ds)
                    
        # pacifico
        pacific = set()
        for i in range(len(heights[0])): # ancho
            dfs(heights,i,0,0,pacific)
        for i in range(len(heights)): # alto
            dfs(heights,0,i,0,pacific)

        # atlantico
        atlantic = set()
        for i in range(len(heights[0])):
            dfs(heights,i,len(heights)-1,0,atlantic)
        for i in range(len(heights)):
            dfs(heights,len(heights[0])-1,i,0,atlantic)

        return list(pacific&atlantic)