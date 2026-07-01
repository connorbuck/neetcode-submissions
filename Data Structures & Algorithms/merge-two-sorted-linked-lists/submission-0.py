# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = None
        prev = None

        # if list1 is empty, return list2
        if list1 is None:
            return list2

        # if list2 is empty, return list1
        if list2 is None:
            return list1

        # compare head value of list1 and list2
        while list1 is not None or list2 is not None:
            if list1 is None:
                prev.next = list2
                return merged_list
            
            if list2 is None:
                prev.next = list1
                return merged_list
            
            if list1.val < list2.val:
                if merged_list is None:
                    merged_list = ListNode(list1.val)
                    prev = merged_list
                    list1 = list1.next
                    continue
                prev.next = list1
                prev = prev.next
                list1 = list1.next
                continue
            
            if merged_list is None:
                merged_list = ListNode(list2.val)
                prev = merged_list
                list2 = list2.next
                continue
            prev.next = list2
            prev = prev.next
            list2 = list2.next
        
        return merged_list
