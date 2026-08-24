# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 1. Create slow and fast
    # 2. while fast is not None (not at the end), advance both slow and fast
    # 3. If slow is None, our list has no cycle (return False)
    # 4. Otherwise, it will get to a point where slow == fast, return True

    # Time: O(n). Space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
        