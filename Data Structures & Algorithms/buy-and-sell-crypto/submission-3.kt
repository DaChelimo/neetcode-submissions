class Solution {
    //     # PLAN
    // # 1. Keep track of the minimum value (minBuy) and maxProfit
    // # 2. Loop through entire list: if value < minBuy, minBuy = value. 
    // #    In every iteration, profit = value - minBuy. If profit > maxProfit, update maxProfit
    // # 3. Return maxProfit

    fun maxProfit(prices: IntArray): Int {
        if (prices.size < 2) return 0

        var minBuy = Int.MAX_VALUE
        var maxProfit = 0

        prices.forEach { price ->
            if (price < minBuy) minBuy = price
            else {
                val profit = price - minBuy
                maxProfit = max(profit, maxProfit)
            }
        }

        return maxProfit
    }
}
