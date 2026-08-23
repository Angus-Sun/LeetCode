class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0
        while q or maxheap:
            time += 1
            if maxheap:
                cnt = 1+heapq.heappop(maxheap)
                if cnt:
                    q.append((time+n, cnt))
            if q and q[0][0] == time:
                heapq.heappush(maxheap, q.popleft()[1])
        return time

