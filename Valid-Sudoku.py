1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        rows = defaultdict(set)
4        cols = defaultdict(set)
5        squares = defaultdict(set)
6
7        for i in range(9):
8            for j in range(9):
9                if board[i][j] == ".":
10                    continue
11                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[i//3, j//3]:
12                    return False
13                rows[i].add(board[i][j])
14                cols[j].add(board[i][j])
15                squares[i//3, j//3].add(board[i][j])
16        return True
17                 
18
19
20            
21                
22