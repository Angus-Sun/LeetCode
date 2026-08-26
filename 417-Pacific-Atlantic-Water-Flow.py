class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        pac, atl = set(), set()
        def dfs(r,c,visited, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or heights[r][c] < prev:
                return
            visited.add((r,c))
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pac, heights[0][c])
            dfs(len(heights)-1, c, atl, heights[len(heights)-1][c])
        for r in range(ROWS):
            dfs(r,0, pac, heights[r][0])
            dfs(r,len(heights[0])-1, atl, heights[r][len(heights[0])-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res