class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(n, c, p):
            if n == 0 and c == 0:
                res.append(p)
                return
            if n > 0:
                p += "("
                dfs(n-1, c+1, p)
                p = p[:len(p)-1]
            if c > 0:
                p += ")"
                dfs(n, c-1, p)
                p = p[:len(p)-1]
        dfs(n,0,"")
        return res

            
