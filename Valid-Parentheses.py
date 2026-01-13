1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        bracket_map = {"]" : "[", "}" : "{", ")" : "("}
5        for c in s:
6            if c in bracket_map:
7                if stack and stack[-1] == bracket_map[c]:
8                    stack.pop()
9                else:
10                    return False
11            else: 
12                stack.append(c)
13        return True if not stack else False