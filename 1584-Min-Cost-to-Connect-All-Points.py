class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]
                dst = abs(xi-xj) + abs(yi-yj)
                adj[i].append((dst, j))
                adj[j].append((dst, i))
        
        visited = set()
        res = 0
        minHeap = [(0, 0)]
        while len(visited) < len(points):
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for c, n in adj[node]:
                heapq.heappush(minHeap, (c,n))
        return res