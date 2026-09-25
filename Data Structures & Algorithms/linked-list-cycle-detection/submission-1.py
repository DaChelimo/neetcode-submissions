# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Create two nodes: slow and fast
    # Move both of them
    # If fast == None, return false
    # If slow == fast, return true

    # Edge cases: 
    # 1. Empty list or singleton => return false
    
    # Time: O(n). Space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True # Cycle exists
        
        return False

        

        