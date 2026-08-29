class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = defaultdict(list)
        visited, cycle = set(), set()
        res = []
        for pair in prerequisites:
            premap[pair[0]].append(pair[1])
        def dfs(i):
            if i in cycle:
                return False
            if i in visited:
                return True
            cycle.add(i)
            for j in premap[i]:
                if not dfs(j):
                    return False
            cycle.remove(i)
            visited.add(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res