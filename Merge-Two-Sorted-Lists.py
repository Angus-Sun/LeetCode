1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = node = ListNode()
9        while list1 and list2:
10            if list1.val < list2.val:
11                node.next = list1
12                list1 = list1.next
13            else:
14                node.next = list2
15                list2 = list2.next
16            node = node.next
17        node.next = list1 or list2
18        return dummy.next