class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, value: int) -> None:
        if not self.minstack:
            self.minstack.append(value)
        else:
            if value < self.minstack[-1]:
                self.minstack.append(value)
            else:
                self.minstack.append(self.minstack[-1])
        self.stack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()