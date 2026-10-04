class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        # Left -> LRU and Right -> MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    # Inserts key to the right of linked list (MRU)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    # Removes any node from its position in the linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            
            node = self.cache[key]
            self.insert(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
        
