# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            newHead = ListNode(0)
            temp = newHead
            
            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                    
                else:
                    temp.next = l2
                    l2 = l2.next
                
                temp = temp.next
            
            if l1 is not None:
                temp.next = l1
            else:
                temp.next = l2
            return newHead.next
        