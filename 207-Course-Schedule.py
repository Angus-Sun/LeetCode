class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        prereqs = defaultdict(list)
        for pair in prerequisites:
            prereqs[pair[0]].append(pair[1])
        def dfs(i):
            if i in visited:
                return False
            if prereqs[i] == []:
                return True
            visited.add(i)
            for j in prereqs[i]:
                if not dfs(j):
                    return False
            visited.remove(i)
            prereqs[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True