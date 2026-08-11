class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif t == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif t == "-":
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(first-second)
            elif t == "/":
                second, first = int(stack.pop()), int(stack.pop())
                stack.append(int(float(first) / second))
            else:
                stack.append(int(t))
        return stack[-1]