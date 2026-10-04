from heapq import heapify, heappop, heappush

class KthLargest:

    # Heap problem. K-th largest integer
    # Flip all the nums to negatives, and when fetching a number

    def __init__(self, k: int, nums: List[int]):
        minHeap = [(x * -1, i) for i, x in enumerate(nums)]
        heapify(minHeap)

        self.count = len(nums)
        self.k = k
        self.minHeap = minHeap
        

    def add(self, val: int) -> int:
        heappush(self.minHeap, (val * -1, self.count))
        temp = []
        self.count += 1

        i = 0
        while i < self.k:
            (value, count) = heappop(self.minHeap)
            temp.append((value, count))
            i += 1
        
        output = temp[-1][0]

        for elem in temp:
            heappush(self.minHeap, elem)

        return output * -1

        
