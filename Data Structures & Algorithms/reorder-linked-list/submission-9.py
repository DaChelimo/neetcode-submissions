# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 1. Find the middle of the list
    # 2. Reverse the second half
    # 3. Merge the two lists
    
    # Edge cases: Empty/Singleton -> return head
    # Time: O(n). Space: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head

        # 1, 2, 3, 4 (1st middle) => 1 -> 2   4 -> 3 ... 2 -> 3
        # 1, 2, 3, 4, 5 => 1, 2, 3 ... 5, 4
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow
        nxt = middle.next
        middle.next = None


        prev = None
        curr = nxt

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr = first = head
        second = prev

        while first and second:
            tmp1 = first.next
            tmp2 = second.next

            curr.next = first
            curr = curr.next
            curr.next = second
            curr = curr.next

            first = tmp1
            second = tmp2

        curr.next = first if first else second
       

        



        