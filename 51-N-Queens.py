class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]* n for i in range(n)]
        cols = set()
        positiveDiag = set()
        negativeDiag = set()
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c not in cols and r+c not in positiveDiag and r-c not in negativeDiag:
                    board[r][c] = "Q"
                    cols.add(c)
                    positiveDiag.add(r+c)
                    negativeDiag.add(r-c)
                    backtrack(r+1)
                    board[r][c] = "."
                    cols.remove(c) 
                    positiveDiag.remove(r+c)
                    negativeDiag.remove(r-c)
        backtrack(0)
        return res
