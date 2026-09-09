class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val result = IntArray(temperatures.size)
        val stack = mutableListOf<Pair<Int, Int>>() // (temp, index)

        temperatures.forEachIndexed { index, temp ->
            while (!stack.isEmpty() && stack.last().component1() < temp) {
                var (ptemp, pindex) = stack.removeLast()
                result[pindex] = index - pindex
            }

            stack.add(temp to index)
        }

        return result
    }
}
