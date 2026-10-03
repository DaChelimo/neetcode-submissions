from heapq import heapify, heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    # Create a list and store the first value in all the lists
    # At every step, make sure to negate the value before adding to the heap
    # Storing structure: (value, next value, index of array)
    # Heapify the list (based on value)
    # While heap is not null, get the min, add it to result, and push the 
    #  next index's value to the heap
    
    # Time: O(k) + O(n log k)
    # Space: O(k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        result = []

        curr = dummy = ListNode()

        for list_index, list_head in enumerate(lists):
            if list_head:
                minHeap.append((list_head.val, list_index, list_head.next))
        
        heapify(minHeap)

        while minHeap:
            value, indexOfList, nextNode = heappop(minHeap)

            curr.next = ListNode(value)
            curr = curr.next
            # result.append(value)

            # # Check if the nextIndex is valid
            # if nextIndex < len(lists[indexOfList]):
            if nextNode:
                valueToAddToHeap = nextNode.val
                heappush(minHeap, (valueToAddToHeap, indexOfList, nextNode.next))
            
        
        # i = 0

        # while i < len(result):
        #     curr.next = ListNode(result[i])
        #     curr = curr.next
        #     i += 1
        
        return dummy.next


        