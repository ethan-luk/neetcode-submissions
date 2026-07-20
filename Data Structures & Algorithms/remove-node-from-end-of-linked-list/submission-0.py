# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur: 
            length += 1
            cur = cur.next

        targetNode = length - n

        if targetNode == 0: return head.next

        prev = None
        cur = head

        while targetNode > 0:
            targetNode -= 1
            prev = cur
            cur = cur.next
        
        # remove
        prev.next = cur.next
        return head