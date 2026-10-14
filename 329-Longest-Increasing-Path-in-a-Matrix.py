class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS,COLS = len(matrix), len(matrix[0])
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        dp = {} # r,c : longest path from there
        def dfs(r,c):  
            if (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] = 1
            for dr, dc in directions:
                new_r, new_c = r+dr, c + dc
                if new_c >= 0 and new_c < COLS and new_r >= 0 and new_r < ROWS and matrix[new_r][new_c] > matrix[r][c]:
                    dp[(r,c)] = max(dp[(r,c)], 1+dfs(new_r,new_c))
            return dp[(r,c)]
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c)
        return max(dp.values())