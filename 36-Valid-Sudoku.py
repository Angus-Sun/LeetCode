class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #looks like a problem that coudl be solved using hashset
        #we basically have a set for rows, cols, and square 
        #square can basically we floor divide row number by 3 and col number by 3 
        # if at any point while were checking the number its in anyof the three sets
        # we know it is invalid
        # gg frickin ezzz

        #oh wait and always a 9x9 board say lesss

        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True 
        
