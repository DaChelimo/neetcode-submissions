from heapq import heapify, heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper():
        def __init__(self, node, count):
            self.node = node
            self.count = count
        
        def __lt__(self, other):
            return (self.node.val, self.count) < (other.node.val, other.count)

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
        count = 0

        curr = dummy = ListNode()

        for head in lists:
            if head:
                minHeap.append(NodeWrapper(head, count))
                count += 1
        
        heapify(minHeap)

        while minHeap:
            node_wrapper = heappop(minHeap)

            curr.next = node_wrapper.node
            curr = curr.next

            nextNode = node_wrapper.node.next
            if nextNode:
                valueToAddToHeap = nextNode.val
                heappush(minHeap, NodeWrapper(nextNode, count))
                count += 1
        
        return dummy.next


        