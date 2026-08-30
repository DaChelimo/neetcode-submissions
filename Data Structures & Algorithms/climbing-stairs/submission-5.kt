class Solution {
    fun climbStairs(n: Int): Int {
        val memo = mutableMapOf<Int, Int>()

        fun dfs(total: Int): Int {
            if (total == n)  return 1
            if (total > n) return 0

            if (memo.contains(total)) return memo[total]!!

            memo[total] = dfs(total + 1) + dfs(total + 2)
            return memo[total]!!
        }

        return dfs(0)
    }
}
