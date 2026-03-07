1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        stack = []
4        pairs = [[p,s] for p,s in zip(position, speed)]
5        pairs.sort()
6        pairs = pairs[::-1]
7        for p, s in pairs:
8            stack.append((target-p)/s)
9            if (len(stack) > 1 and stack[-1] <= stack[-2]):
10                stack.pop()
11        return len(stack)