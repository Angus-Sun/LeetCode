class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i,t = stack.pop()
                diff = index - i
                res[i] = diff
            stack.append((index, temp))
        return res

        #index 0 temperature 73
        # [73, 0]
        # index 1 74
        # i,t = 73, 0
        # 1 - 0
        # 1
        #[74,1]
        # i,t = 74,1
        # diff 2 - 1 = 1
        # 1

