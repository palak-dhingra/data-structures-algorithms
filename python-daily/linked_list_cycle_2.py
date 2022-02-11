# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        totto = head
        rabit = head
        
        if totto is None:
            return None
        
        while True:
            totto = totto.next
            if rabit is None or rabit.next is None:
                return None
            rabit = rabit.next.next
            
            if totto == rabit:
                break
        rabit = head
        while rabit!=totto:
            totto = totto.next
            rabit = rabit.next
            
        return totto
        