# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        S, F = head, head
        length = 1

        if not head.next:
            return None
        
        while F.next:
            if not F.next.next:
                # only can advance fast pointer by 1
                F = F.next
                length += 1
                continue
            length += 2
            F = F.next.next
        
        # remove head node
        if length - n == 0:
            head = head.next
            return head
        
        moves_to_make = length - n
        moves = 0
        prev = S
        while moves < moves_to_make:
            prev = S
            S = S.next
            moves += 1
        
        temp = S.next
        prev.next = temp
        S.next = None

        return head