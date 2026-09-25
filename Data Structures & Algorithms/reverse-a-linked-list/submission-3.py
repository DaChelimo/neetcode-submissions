# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Check if the head is empty or has no next (means it is a singleton or null), and return the head if true
    # Create prev = dummy and curr = head
    # Loop through the list
    #  1. Store the next pointer in tmp
    #  2. Modify the pointer's next to point to prev
    #  3. Assign prev to curr
    #  4. Assign curr to next
    
    # Time: O(n). Space: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
        