1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stack = []
4        res = [0] * len(temperatures)
5        for i, t in enumerate(temperatures):
6            while (stack and t > stack[-1][0]):
7                temp, index = stack.pop()
8                res[index] = i - index
9            stack.append([t, i])
10        return res