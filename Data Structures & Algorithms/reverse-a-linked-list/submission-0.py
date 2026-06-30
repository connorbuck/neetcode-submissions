# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        prev = None

        while head:
            stack.append(head.val)
            head = head.next
        
        if len(stack) == 0:
            return head

        new_head = ListNode(stack.pop())
        prev = new_head
        while stack:
            node = ListNode(stack.pop())
            prev.next = node
            prev = node
        
        return new_head