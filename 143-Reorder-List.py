# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        previous = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        previous = slow
        curr, prev = slow.next, None
        previous.next = None
        while curr:
            temp = prev
            prev = curr
            curr = curr.next
            prev.next = temp
        #1,2,3,4
        curr = head
        while prev:
            previous = curr   #previous = 1
            curr = curr.next #curr = 2
            previous.next = prev #1->4
            current = prev #4
            prev = prev.next #3
            current.next = curr #4-2
        
        return head
        
        