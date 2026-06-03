1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        oldToNew = {None: None}
13        curr = head
14        while curr:
15            oldToNew[curr] = Node(curr.val, None, None)
16            curr = curr.next
17        curr = head
18        while curr:
19            oldToNew[curr].next = oldToNew[curr.next]
20            oldToNew[curr].random = oldToNew[curr.random]
21            curr = curr.next
22        return oldToNew[head]