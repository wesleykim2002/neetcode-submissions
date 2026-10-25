class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            else:
                grid[x][y] = 0
                return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))
        
        return area