class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        minHeap = [(grid[0][0], 0, 0)] # time, row, col
        visited.add((0,0))
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if r == ROWS-1 and c == COLS-1:
                return time
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or (new_r, new_c) in visited:
                    continue
                visited.add((new_r, new_c))
                heapq.heappush(minHeap, (max(time, grid[new_r][new_c]), new_r, new_c))

