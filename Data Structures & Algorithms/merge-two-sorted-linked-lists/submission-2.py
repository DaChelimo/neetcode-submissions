# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 1. Create two pointers: one for list1 and another for list2
    # 2. While both are non-null, compare the values of both nodes, and pick the smaller one, and then advance the smaller pointer forward
    # 3. Once the loop finishes, it means one of them run out of values, append the other one to the end of the result list

    # Edge cases: One empty, or both empty.
    # Time: O(n). Space: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        first = list1
        second = list2
        dummy = result = ListNode(0)

        while first and second:
            if first.val < second.val:
                node = first
                first = first.next
            else:
                node = second
                second = second.next
            
            result.next = node
            result = result.next
        
        result.next = first if first else second
        return dummy.next

        

        