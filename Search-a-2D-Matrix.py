1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        ROWS, COLS = len(matrix), len(matrix[0])
4        bottom, top = 0, ROWS-1
5        while bottom <= top:
6            mid = bottom + (top-bottom)//2
7            if target < matrix[mid][0]:
8                top = mid-1
9            elif target > matrix[mid][COLS-1]:
10                bottom = mid+1
11            else:
12                l, r = 0, COLS-1
13                while (l <= r):
14                    m = l + (r-l) // 2
15                    if matrix[mid][m] == target:
16                        return True
17                    elif target > matrix[mid][m]:
18                        l = m + 1
19                    else:
20                        r = m - 1 
21                return False
22        return False