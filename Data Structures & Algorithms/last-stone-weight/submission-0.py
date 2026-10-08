from heapq import heapify, heappop, heappush

class Solution:
    # Create a max heap (build a min heap with values negated)
    # While heapsize > 1: 
    #   get the two largest stones (and reverse the value)
    #   if equal, continue;
    #   if x < y, let new = y - x, negate new and add to heap.push()
    # Return heap.pop or 0 if empty
    
    # Time: O(n lg n). Space: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-stone for stone in stones]
        heapify(minHeap)
        heapsize = len(minHeap)

        while heapsize > 1:
            first = heappop(minHeap)
            second = heappop(minHeap)

            if first == second:
                heapsize -= 2

            x, y = min(first, second), max(first, second)
            if x < y:
                new = y - x
                heappush(minHeap, -new)
                heapsize -= 1
        
        return -heappop(minHeap) if heapsize == 1 else 0

