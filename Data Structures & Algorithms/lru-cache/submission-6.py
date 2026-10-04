class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    # Insert to the MRU
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    # Remove node anywhere in linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if not key in self.cache and len(self.cache) == self.capacity:
            # Remove LRU
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key, None)
        
        if key in self.cache: # Update MRU still
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
