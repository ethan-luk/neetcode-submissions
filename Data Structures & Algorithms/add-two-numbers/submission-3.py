# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2

        dummy = curNode = ListNode()

        carry = False
        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            
            s = v1 + v2 + carry
            carry = s // 10
            s = s % 10
            newNode = ListNode(val=s)
            curNode.next = newNode
            curNode = newNode
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        
        # if not p1 and not p2 and carry:
        #     newNode = ListNode(val=1)
        #     curNode.next = newNode

        # while p1:
        #     num_to_add = p1.val
        #     if carry:
        #         num_to_add += 1
        #         carry = False
        #     newNode = ListNode(val=num_to_add)
        #     curNode.next = newNode
        #     curNode = newNode
        #     p1 = p1.next

        # while p2:
        #     num_to_add = p2.val
        #     if carry:
        #         num_to_add += 1
        #         carry = False
        #     newNode = ListNode(val=num_to_add)
        #     curNode.next = newNode 
        #     curNode = newNode
        #     p2 = p2.next 

        return dummy.next 