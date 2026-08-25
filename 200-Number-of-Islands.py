class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for c in range(COLS)] for r in range(ROWS)]
        res = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or visited[r][c] or grid[r][c] == "0":
                return False
            visited[r][c] = True
            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return True
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c):
                    res += 1
        return res
            