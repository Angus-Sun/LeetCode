1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        slow, fast = head, head
10        while fast and fast.next:
11            slow = slow.next
12            fast = fast.next.next
13            if slow == fast:
14                return True
15        return False