# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next is None:
            return None
        
        k = 0
        temp = head
        while temp!=None:
            k += 1
            temp = temp.next
            
        
        temp = head
        if k==n:
            return head.next
        jumps = k - n - 1
        while jumps>0:
            jumps -=1
            temp = temp.next
        
        temp.next = temp.next.next
        
        return head