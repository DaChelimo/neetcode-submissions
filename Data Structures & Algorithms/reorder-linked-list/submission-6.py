# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # PLAN
    # 1. Find the middle node and split in half
    # 2. Reverse the second half
    # 3. Merge the second list with the first list

    # REMEMBER: Odd, middle. Even, second middle. Middle is part of second list
    # HENCE: [1, 2, 3, 4] -> [1, 4, 2, 3] and [1, 2, 3, 4, 5] -> [1, 5, 2, 4, 3]

    # EDGE CASES:
    # 1. Singleton list

    # Time: O(n). Space: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head.next:
        #     return

        # Find before middle
        slow, fast = head, head.next

        while fast and fast.next:            
            slow = slow.next
            fast = fast.next.next

        
        # Reverse middle onwards
        curr = middle = slow.next # Start at the new middle
        prev = slow.next = None # Remove connection between first and second half


        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Merge alternately
        node = dummy = ListNode()
        first = head
        second = prev

        while first and second:
            first_next, second_next = first.next, second.next

            node.next = first
            node = node.next

            node.next = second
            node = node.next
            
            first = first_next
            second = second_next
        
        node.next = first if first else second
