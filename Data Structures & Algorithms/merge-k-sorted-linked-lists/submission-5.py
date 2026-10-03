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
        minHeap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapify(minHeap)

        count = len(lists)
        curr = dummy = ListNode()

        while minHeap:
            (value, _, node) = heappop(minHeap)

            curr.next = node
            curr = curr.next

            nextNode = node.next
            if nextNode:
                heappush(minHeap, (nextNode.val, count, nextNode))
                count += 1
        
        return dummy.next


        