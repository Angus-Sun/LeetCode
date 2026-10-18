class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        moves = [len(matrix[0]), len(matrix)-1]
        r,c,d = 0, -1, 0
        res = []
        while moves[d&1]:
            for i in range(moves[d&1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            moves[d&1] -= 1
            d = (d+1) % 4
        return res