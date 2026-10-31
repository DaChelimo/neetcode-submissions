data class Node(
    val key: Int, 
    val value: Int, 
    var prev: Node? = null, 
    var next: Node? = null
    )

class LRUCache(capacity: Int) {
    val capacity = capacity
    val cache = hashMapOf<Int, Node>()
    val left = Node(0, 0)
    val right = Node(0,0)

    init {
        left.next = right
        right.prev = left
    }

    fun remove(node: Node?) {
        val prev = node?.prev
        val nxt = node?.next
        prev?.next = nxt
        nxt?.prev = prev
    }
    fun insert(node: Node) {
        val prev = right.prev
        val nxt = right

        node.prev = prev
        node.next = nxt

        prev?.next = node
        nxt?.prev = node
    }

    fun get(key: Int): Int {
        if (key !in cache) {
            return -1
        }
        
        val node = cache[key]!!
        remove(node)
        insert(node)

        return node.value
    }

    fun put(key: Int, value: Int) {
        if (key in cache) {
            remove(cache[key])
        }
        val newNode = Node(key, value)
        cache[key] = newNode
        insert(newNode)

        if (cache.size > capacity) {
            val lru = left.next
            remove(lru)
            lru?.key?.let { cache.remove(it) }
        }
    }
}
