class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    # Remove from linkedList
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert at the right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

        if len(self.cache) == self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)
        

