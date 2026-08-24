# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # INPUT: Two sorted lists
    # OUTPUT: One sorted combined list

    # REMEMBER: Either list could be empty
    #
    # PLAN :
    # 1. Create two pointers (one per list), and result list
    # 2. Compare the values at the two pointers, and append the smaller one to result
    # 3. Move the smaller pointer forward, and then repeat
    # 4. Stop when both pointers are at the end
    # 5. In iteration, check if either list is at its end, and if true, just extend the 
    # result with the remaining other list
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     listA = list1
    #     listB = list2

    #     dummy = ListNode(None, next = None)
    #     curr = dummy

    #     while listA and listB:
    #         if (listA.val <= listB.val):
    #             curr.next = listA
    #             curr = curr.next
    #             listA = listA.next
    #         else:
    #             curr.next = listB 
    #             curr = curr.next
    #             listB = listB.next
        
    #     remaining = listA if listA else listB
    #     curr.next = remaining

    #     return dummy.next


    # Recursively
    # Imagine: [1 -> 4], [2 -> 3 -> 5]
    # Base Case: not listA and not listB -> None
    #            not listA -> listB
    #            not listB -> listA
    # Recursive case:
    # 1. listA.val vs listB.val, pick smaller
    # 2. [e.g A is smaller] Call node.next = merge(listA.next, listB)
    
    # Time: O(n). Space: O(n)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
        

        