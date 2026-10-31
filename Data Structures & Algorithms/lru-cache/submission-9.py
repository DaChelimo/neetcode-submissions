from heapq import heapify, heappush, heappop

class LRUCache:
    def __init__(self, capacity: int):
        self.tracker = {}
        self.minHeap = []
        self.time = 0
        self.capacity = capacity
        # Create hashmap for tracking key: (value, time) pairs
        # MinHeap keyed on time -> (time, key)
        # When cache is full, pop heap. Check if key.time == heap.time
        # If so, pop from both hashmap and heap
        # Else, continue until you find such a situation
        # In every put or get operating, update the key.time variable
        
    # O(1)
    def get(self, key: int) -> int:
        if key not in self.tracker:
            return -1
        
        _, value = self.tracker[key]
        self.tracker[key] = (self.time, value)
        heappush(self.minHeap, (self.time, key))
        self.time += 1
        return value

        

    # Add to heap, update hashmap, check cache and update
    # Time: O(1)
    def put(self, key: int, value: int) -> None:
        if len(self.tracker) == self.capacity and key not in self.tracker:
            while self.minHeap:
                oldTime, oldKey = heappop(self.minHeap)

                if oldTime == self.tracker[oldKey][0]:
                    del self.tracker[oldKey]
                    break
        
        self.tracker[key] = (self.time, value)
        heappush(self.minHeap, (self.time, key))
        self.time += 1
                

        
