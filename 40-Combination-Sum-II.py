class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, arr, total):
            if total >= target or i >= len(candidates):
                if total == target:
                    res.append(arr.copy())
                return
            arr.append(candidates[i])
            dfs(i+1, arr, total+candidates[i])
            arr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, arr, total)
        dfs(0, [], 0)
        return res
            
