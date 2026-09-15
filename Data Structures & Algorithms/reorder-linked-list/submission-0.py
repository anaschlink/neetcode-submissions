# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        head2 = slow.next
        slow.next = None
        current = head2

        while current:
            current_n = current.next
            current.next = prev
            prev = current
            current = current_n
        
        head2 = prev
        p1 = head
        p2 = head2

        while p1 and p2:
            p1_n = p1.next
            p2_n = p2.next
            p1.next = p2
            p2.next = p1_n
            p1 = p1_n
            p2 = p2_n
        
        

        
        