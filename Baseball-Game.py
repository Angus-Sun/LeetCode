1class Solution:
2    def calPoints(self, operations: List[str]) -> int:
3        stack = []
4        for o in operations:
5            if o == "+":
6                stack.append(stack[-1]+stack[-2])
7            elif o == "D":
8                stack.append(2*stack[-1])
9            elif o == "C":
10                stack.pop()
11            else:
12                stack.append(int(o))
13        return sum(stack)