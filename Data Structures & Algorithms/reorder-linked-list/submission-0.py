class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        nodes = []
        head_copy = head

        while head_copy:
            nodes.append(head_copy)
            head_copy = head_copy.next

        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            if l == r:
                break
            nodes[r].next = nodes[l]
            r -= 1
        
        nodes[l].next = None