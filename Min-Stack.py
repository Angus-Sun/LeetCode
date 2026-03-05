1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minStack = []
6
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9        if self.minStack:
10            val = min(val, self.minStack[-1])
11        self.minStack.append(val)
12
13    def pop(self) -> None:
14        self.stack.pop()
15        self.minStack.pop()
16
17    def top(self) -> int:
18        return self.stack[-1]
19
20    def getMin(self) -> int:
21        return self.minStack[-1]
22
23
24# Your MinStack object will be instantiated and called as such:
25# obj = MinStack()
26# obj.push(val)
27# obj.pop()
28# param_3 = obj.top()
29# param_4 = obj.getMin()