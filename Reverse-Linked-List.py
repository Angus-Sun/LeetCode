1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev, curr = None, head
9        while (curr):
10            temp = prev
11            prev = curr
12            curr = curr.next
13            prev.next = temp
14        return prev