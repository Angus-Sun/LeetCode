class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for d in directions:
                    r,c = row + d[0], col + d[1]
                    if r >= 0 and c >= 0 and r < ROWS and c < COLS and grid[r][c] == 1:
                        q.append([r,c])
                        grid[r][c] = 2
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

 
