# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currTotal = total = ListNode(-1)
        curr1 = l1
        curr2 = l2
        

        carryOn = 0

        while curr1 or curr2 or carryOn:
            raw = carryOn
            if curr1:
                raw += curr1.val
            if curr2:
                raw += curr2.val

            value = raw % 10
            carryOn = raw // 10

            newNode = ListNode(value)
            currTotal.next = newNode
            currTotal = currTotal.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        # if carryOn > 0:
        #     currTotal.next = ListNode(carryOn)
            
        return total.next

