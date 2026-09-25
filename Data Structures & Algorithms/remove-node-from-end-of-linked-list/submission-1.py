# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 1. Create a dummy
    # 1b. If check for empty or singleton, and return if that case
    # 1. Create slow, fast
    # 2. Advance fast by n + 1 steps
    # 3. Advance both at the same pace
    # 4. Set the curr node to curr.next.next
    # 5. Return dummy.next

    # Time: O(n). Space: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        # 1, 2 n= 2
        slow = fast = dummy = ListNode(0, head)

        # i = 1 
        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next 
        