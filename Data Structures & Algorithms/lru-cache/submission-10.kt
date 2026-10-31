import java.util.PriorityQueue

class LRUCache(val capacity: Int) {
    val tracker = hashMapOf<Int, Pair<Int, Int>>()
    val minHeap = PriorityQueue<Pair<Int, Int>>(compareBy{ it.first })
    

    var time = 0

    fun get(key: Int): Int {
        if (!(key in tracker)) {
            return -1
        }
        
        val (_, value) = tracker[key]!!
        update(key, value)

        return value
    }

    fun put(key: Int, value: Int) {
        if (!(key in tracker) && tracker.size == capacity) {
            // We are adding a new item... remove the oldest one

            while (!minHeap.isEmpty()) {
                val (oldTime, oldKey) = minHeap.poll()

                if (oldTime == tracker[oldKey]?.first) {
                    tracker.remove(oldKey)
                    break
                }
            }
        }

        update(key, value)
    }

    fun update(key: Int, value: Int) {
        tracker[key] = time to value
        minHeap.add(time to key)
        time += 1
    }
}
