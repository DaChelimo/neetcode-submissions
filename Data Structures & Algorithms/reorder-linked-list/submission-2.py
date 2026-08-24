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

    # Time: O(n). Space: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        # Find middle
        slow = fast = head
        beforeMiddle = None

        while fast and fast.next:
            beforeMiddle = slow
            slow = slow.next
            fast = fast.next.next
        
        middle = slow
        
        if beforeMiddle:
            beforeMiddle.next = None
            print("Before Middle is ", beforeMiddle.val)
        
        print("Middle is ", middle.val)

        # Reverse middle onwards
        prev = None
        curr = middle

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        headOfList2 = prev
        print("headOfList2 is ", headOfList2.val)

        # Merge alternately
        node = dummy = ListNode()
        first = head
        second = headOfList2
        # dummy.next = head

        while node:
            # print("Node is ", node)
            if first:
                node.next = first
                first = first.next
                node = node.next
            else:
                node.next = second
                break

            if second:
                node.next = second
                second = second.next
                node = node.next
            else:
                node.next = first
                break
