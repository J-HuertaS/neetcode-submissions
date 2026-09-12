class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, x, y):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                return False

            if grid[y][x] == "0":
                return False

            grid[y][x] = "0"

            # mover en las cuatro direcciones
            dfs(grid,x+1,y)
            dfs(grid,x-1,y)
            dfs(grid,x,y+1)
            dfs(grid,x,y-1)
        
        counter = 0

        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == "1":
                    counter += 1
                    dfs(grid,i,j)

        return counter

        